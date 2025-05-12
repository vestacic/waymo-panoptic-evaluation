import json
import os
import uuid
from pathlib import Path

import cv2
import dask
import dask.dataframe
import numpy as np
import pandas as pd
import torch
import torchvision


KEY_COLUMNS = [
    "key.segment_context_name",
    "key.frame_timestamp_micros",
    "key.camera_name",
]
IMAGE_COLUMNS = ["[CameraImageComponent].image"]
SEGMENTATION_COLUMNS = [
    "[CameraSegmentationLabelComponent].panoptic_label_divisor",
    "[CameraSegmentationLabelComponent].panoptic_label",
]


def load_parquet_data_dask(
    parquet_path: Path, columns: list[str]
) -> dask.dataframe.DataFrame:
    return dask.dataframe.read_parquet(
        parquet_path, engine="pyarrow", columns=columns
    )


def get_merged_dataframe(
    image_columns: list[str],
    segmentation_columns: list[str],
    key_columns: list[str],
    image_path: Path,
    segmentation_path: Path,
) -> dask.dataframe.DataFrame:
    dask_camera_image_df = load_parquet_data_dask(
        parquet_path=image_path,
        columns=image_columns + key_columns,
    )
    dask_camera_segmentation_df = load_parquet_data_dask(
        parquet_path=segmentation_path,
        columns=segmentation_columns + key_columns,
    )
    return dask.dataframe.merge(
        dask_camera_image_df,
        dask_camera_segmentation_df,
        on=key_columns,
        how="inner",
    )


def get_waymo_image(entry: pd.Series) -> torch.Tensor:
    jpeg_bytes = entry["[CameraImageComponent].image"]

    encoded_tensor = torch.frombuffer(
        buffer=bytearray(jpeg_bytes), dtype=torch.uint8
    )
    image_tensor = torchvision.io.decode_image(
        input=encoded_tensor,
        mode=torchvision.io.ImageReadMode.RGB,
    )
    image = image_tensor.permute(1, 2, 0).numpy()
    return image


def get_waymo_panoptic_label_divisor(entry: pd.Series) -> int:
    return entry["[CameraSegmentationLabelComponent].panoptic_label_divisor"]


def get_waymo_panoptic_label(entry: pd.Series) -> np.ndarray:
    label = np.frombuffer(
        entry["[CameraSegmentationLabelComponent].panoptic_label"],
        dtype=np.uint8,
    )
    cv2_label = cv2.imdecode(label, cv2.IMREAD_UNCHANGED)
    return cv2_label


def main(waymo_data_dir: Path) -> None:
    raw_image_path = waymo_data_dir / "raw_images"
    image_path = waymo_data_dir / "images"
    segmentation_path = waymo_data_dir / "segmentations"
    merged_df = get_merged_dataframe(
        image_columns=IMAGE_COLUMNS,
        segmentation_columns=SEGMENTATION_COLUMNS,
        key_columns=KEY_COLUMNS,
        image_path=raw_image_path,
        segmentation_path=segmentation_path,
    )
    unique_entries_df = merged_df[KEY_COLUMNS].drop_duplicates().compute()

    image_path.mkdir(parents=True, exist_ok=True)

    panoptic_labels_dir = waymo_data_dir / "panoptic_labels"
    panoptic_labels_dir.mkdir(parents=True, exist_ok=True)

    metadata = {"data": []}

    for index, row in unique_entries_df.iterrows():
        context = row["key.segment_context_name"]
        timestamp = row["key.frame_timestamp_micros"]
        camera_name = row["key.camera_name"]

        entry = (
            merged_df[
                (merged_df["key.segment_context_name"] == context)
                & (merged_df["key.frame_timestamp_micros"] == timestamp)
                & (merged_df["key.camera_name"] == camera_name)
            ]
            .compute()
            .iloc[0]
        )

        image = get_waymo_image(entry)
        panoptic_label_divisor = get_waymo_panoptic_label_divisor(entry)
        panoptic_label = get_waymo_panoptic_label(entry)

        id = uuid.uuid4()
        image_file_name = f"{id}.jpg"
        panoptic_label_file_name = f"{id}.png"

        data = {
            "image_file_name": image_file_name,
            "panoptic_label_file_name": panoptic_label_file_name,
            "panoptic_label_divisor": int(panoptic_label_divisor),
            "context": context,
            "timestamp": timestamp,
            "camera_name": camera_name,
        }

        metadata["data"].append(data)

        cv2.imwrite(
            image_path / image_file_name,
            cv2.cvtColor(image, cv2.COLOR_RGB2BGR),
        )
        cv2.imwrite(
            panoptic_labels_dir / panoptic_label_file_name, panoptic_label
        )

        print(f"Processed: {data}")

    with open(waymo_data_dir / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":
    waymo_data_dir = os.environ.get(
        "WAYMO_DATA_DIR", Path(__file__).parents[2] / "waymo_data"
    )
    main(waymo_data_dir=waymo_data_dir)
