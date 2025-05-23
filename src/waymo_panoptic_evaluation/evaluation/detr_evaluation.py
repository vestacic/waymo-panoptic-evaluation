import os
import time
import warnings
from pathlib import Path

import torch
from torch.utils.data import DataLoader
from torchmetrics.detection import PanopticQuality
from transformers import DetrForSegmentation, DetrImageProcessor

from waymo_panoptic_evaluation import mappings
from waymo_panoptic_evaluation.waymo_dataset import WaymoDataset

warnings.filterwarnings("ignore", message=".*copying from a non-meta parameter.*")

def evaluate_detr(dataset_path: Path, output_path: str ="detr_evaluation_results.txt") -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[INFO] Running on {device}")

    dataset = WaymoDataset(image_directory=dataset_path)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False, num_workers=1)

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50-panoptic")
    model = DetrForSegmentation.from_pretrained("facebook/detr-resnet-50-panoptic")
    model.eval()
    model.to(device)

    print("[INFO] Model created. Running evaluation...")

    pq_metric = PanopticQuality(
        things=mappings.WAYMO_THING_CLASSES_IDS,
        stuffs=mappings.WAYMO_STUFF_CLASSES_IDS,
        return_sq_and_rq=True,
        return_per_class=False,
    ).to(device)

    pq_metric_per_class = PanopticQuality(
        things=mappings.WAYMO_THING_CLASSES_IDS,
        stuffs=mappings.WAYMO_STUFF_CLASSES_IDS,
        return_sq_and_rq=False,
        return_per_class=True,
    ).to(device)

    start_time = time.time()
    with torch.no_grad():
        for i, (img, (gt_sem, gt_inst)) in enumerate(dataloader):
            img = img.to(device)
            inputs = processor(images=img, return_tensors="pt").to(device)
            outputs = model(**inputs)

            semantic_mask = gt_sem.to(device)
            instance_mask = gt_inst.to(device)
            height, width = semantic_mask.shape[-2:]
            result = processor.post_process_panoptic_segmentation(outputs, target_sizes=[(height, width)])[0]

            pred_mask = result["segmentation"].to(device)
            pred_segments_info = result["segments_info"]

            pred_panoptic_tensor = torch.zeros((height, width, 2), dtype=torch.long, device=device)
            class_instance_counter = {}

            for seg in pred_segments_info:
                mask = pred_mask == seg["id"]
                if not mask.any():
                    continue

                coco_id = seg["label_id"]
                waymo_id = mappings.COCO_ID_TO_WAYMO_ID.get(coco_id, 0)
                if waymo_id == 0:
                    continue

                pred_panoptic_tensor[..., 0][mask] = waymo_id
                if waymo_id in mappings.WAYMO_STUFF_CLASSES_IDS:
                    pred_panoptic_tensor[..., 1][mask] = 0
                else:
                    if waymo_id not in class_instance_counter:
                        class_instance_counter[waymo_id] = 1
                    else:
                        class_instance_counter[waymo_id] += 1
                    instance_id = class_instance_counter[waymo_id]
                    pred_panoptic_tensor[..., 1][mask] = instance_id

            gt_panoptic_tensor = torch.stack((semantic_mask.squeeze(0), instance_mask.squeeze(0)), dim=-1).to(torch.long)
            # visualize_masks(semantic_mask, instance_mask, pred_panoptic_tensor) #Usage example
            pq_metric.update(
                pred_panoptic_tensor.unsqueeze(0),
                gt_panoptic_tensor.unsqueeze(0)
            )
            pq_metric_per_class.update(
                pred_panoptic_tensor.unsqueeze(0),
                gt_panoptic_tensor.unsqueeze(0)
            )
            if (i + 1) % 300 == 0:
                print(f"[INFO] Processed {i + 1} images...")

    total_time = time.time() - start_time

    final_pq = pq_metric.compute()

    per_class_pq = pq_metric_per_class.compute().squeeze(0)
    all_class_ids = mappings.WAYMO_THING_CLASSES_IDS + mappings.WAYMO_STUFF_CLASSES_IDS
    per_class_pq_sorted = list(zip(all_class_ids, per_class_pq.tolist()))
    per_class_pq_sorted.sort(key=lambda x: x[0], reverse=False) 

    print("DETR Panoptic Quality Evaluation")
    print(f"PQ: {final_pq[0].item():.4f}")
    print(f"SQ: {final_pq[1].item():.4f}")
    print(f"RQ: {final_pq[2].item():.4f}")
    print(f"[TIMER] Evaluation loop took {total_time:.2f} seconds")

    with open(output_path, "w") as f:
        f.write("DETR Panoptic Quality Evaluation\n")
        f.write(f"PQ: {final_pq[0]:.4f}\n")
        f.write(f"SQ: {final_pq[1]:.4f}\n")
        f.write(f"RQ: {final_pq[2]:.4f}\n")
        f.write(f"TIMER: Evaluation loop took {total_time:.2f} minutes\n")
        f.write("\nPer-class Panoptic Quality (Class ID, PQ):\n")
        for class_id, pq_val in per_class_pq_sorted:
            f.write(f"{class_id} {pq_val:.4f}\n")

    print(f"[INFO] Results saved to {output_path}")

if __name__ == "__main__":
    evaluate_detr(os.environ.get(
            "WAYMO_DATA_DIR", Path(__file__).parents[3] / "waymo_data"
        )
    )
