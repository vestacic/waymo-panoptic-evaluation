import json
from pathlib import Path

import cv2
import numpy as np
from torch.utils.data import Dataset


class WaymoDataset(Dataset):
    def __init__(self, image_directory: Path, color_conversion=None) -> None:
        self.dir = image_directory
        self.color_conversion = color_conversion

        with open(self.dir / "metadata.json", "r") as f:
            self.metadata = json.load(f)["data"]

    def __len__(self) -> int:
        return len(self.metadata)

    def __getitem__(
        self, idx: int
    ) -> tuple[np.ndarray, tuple[np.ndarray, np.ndarray]]:
        item_metadata = self.metadata[idx]
        image_path = self.dir / "images" / item_metadata["image_file_name"]
        panoptic_label_path = (
            self.dir
            / "panoptic_labels"
            / item_metadata["panoptic_label_file_name"]
        )
        panoptic_label_divisor = item_metadata["panoptic_label_divisor"]

        image = cv2.imread(image_path)
        if self.color_conversion is not None:
            image = cv2.cvtColor(image, self.color_conversion)

        panoptic_label = cv2.imread(panoptic_label_path, cv2.IMREAD_UNCHANGED)

        semantic_mask = panoptic_label // panoptic_label_divisor
        instance_mask = panoptic_label % panoptic_label_divisor

        return image, (semantic_mask, instance_mask)
