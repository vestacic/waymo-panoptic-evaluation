import os
from pathlib import Path

import torch
import torchmetrics
from torch.utils.data import DataLoader
from transformers import (
    AutoImageProcessor,
    Mask2FormerForUniversalSegmentation,
)

from waymo_panoptic_evaluation import mappings
from waymo_panoptic_evaluation.waymo_dataset import WaymoDataset


def evaluate_mask2former(waymo_data_dir: Path) -> None:
    dataset = WaymoDataset(image_directory=waymo_data_dir)
    dataloader = DataLoader(
        dataset, batch_size=1, shuffle=False, num_workers=4
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_checkpoint = "facebook/mask2former-swin-large-ade-panoptic"
    processor = AutoImageProcessor.from_pretrained(model_checkpoint)
    model = Mask2FormerForUniversalSegmentation.from_pretrained(
        model_checkpoint
    )
    model.to(device)
    model.eval()

    panoptic_quality_metric = torchmetrics.detection.PanopticQuality(
        things=mappings.WAYMO_THING_CLASSES_IDS,
        stuffs=mappings.WAYMO_STUFF_CLASSES_IDS,
        return_sq_and_rq=True,
        return_per_class=False,
    ).to(device)

    with torch.no_grad():
        for image, masks in dataloader:
            semantic_mask, instance_mask = masks
            # move to device
            image = image.to(device)
            image = image.squeeze(0)
            semantic_mask = semantic_mask.to(device)
            instance_mask = instance_mask.to(device)

            # preprocess inputs
            inputs = processor(images=image, return_tensors="pt")
            pixel_values = inputs["pixel_values"].to(device)
            model_inputs = {"pixel_values": pixel_values}

            outputs = model(**model_inputs)

            # postprocess outputs
            original_height, original_width = semantic_mask.shape[-2:]
            panoptic_results = processor.post_process_panoptic_segmentation(
                outputs, target_sizes=[(original_height, original_width)]
            )

            result = panoptic_results[0]
            predicted_segmentation_map = result["segmentation"].to(device)
            segments_info = result["segments_info"]

            pred_panoptic_tensor = torch.zeros(
                (original_height, original_width, 2),
                dtype=torch.long,
                device=device,
            )
            for segment in segments_info:
                mask = predicted_segmentation_map == segment["id"]
                if not mask.any():
                    print("empty mask")
                    continue
                ade_label_id = segment["label_id"]
                waymo_label_id = mappings.ADE20K_TO_WAYMO.get(ade_label_id, 0)

                if waymo_label_id == 0:
                    continue
                pred_panoptic_tensor[..., 0][mask] = waymo_label_id
                pred_panoptic_tensor[..., 1][mask] = segment["id"]

                if waymo_label_id in mappings.WAYMO_STUFF_CLASSES_IDS:
                    pred_panoptic_tensor[..., 1][mask] = 0
                else:
                    pred_panoptic_tensor[..., 1][mask] = segment["id"]

            target_panoptic_tensor = torch.stack(
                (semantic_mask.squeeze(0), instance_mask.squeeze(0)),
                dim=-1,
            ).to(torch.long)
            pred_panoptic_tensor = pred_panoptic_tensor.to(torch.long)

            panoptic_quality_metric.update(
                pred_panoptic_tensor.unsqueeze(0),
                target_panoptic_tensor.unsqueeze(0),
            )
    final_pq_results = panoptic_quality_metric.compute()
    print(final_pq_results)
    print(f"Panoptic Quality (PQ): {final_pq_results[0].item():.4f}")
    print(f"Segmentation Quality (SQ): {final_pq_results[1].item():.4f}")
    print(f"Recognition Quality (RQ): {final_pq_results[2].item():.4f}")


if __name__ == "__main__":
    evaluate_mask2former(
        waymo_data_dir=os.environ.get(
            "WAYMO_DATA_DIR", Path(__file__).parents[3] / "waymo_data"
        )
    )
