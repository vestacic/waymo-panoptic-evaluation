import os
import time
from pathlib import Path
from pprint import pprint

import torch
from detectron2 import model_zoo
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.modeling import build_model
from torch.utils.data import DataLoader
from torchmetrics.detection import PanopticQuality

from waymo_panoptic_evaluation import mappings
from waymo_panoptic_evaluation.waymo_dataset import WaymoDataset


def evaluate_panopticfpn(waymo_data_dir: Path) -> None:
    dataset = WaymoDataset(image_directory=waymo_data_dir)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False, num_workers=4)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    cfg = get_cfg()
    cfg.merge_from_file(
        model_zoo.get_config_file(
            "COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"
        )
    )
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(
        "COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"
    )
    cfg.MODEL.DEVICE = device.type
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5

    metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
    thing_classes = metadata.thing_classes
    stuff_classes = metadata.stuff_classes

    model = build_model(cfg).to(device)
    DetectionCheckpointer(model).load(cfg.MODEL.WEIGHTS)

    model.eval()

    pq_metric_avg = PanopticQuality(
        things=mappings.WAYMO_THING_CLASSES_IDS,
        stuffs=mappings.WAYMO_STUFF_CLASSES_IDS,
        return_sq_and_rq=True,
        return_per_class=False,
    ).to(device)
    pq_metric_per_class = PanopticQuality(
        things=mappings.WAYMO_THING_CLASSES_IDS,
        stuffs=mappings.WAYMO_STUFF_CLASSES_IDS,
        return_sq_and_rq=True,
        return_per_class=True,
    ).to(device)

    start_time = time.time()
    with torch.no_grad():
        for original_image, masks in dataloader:
            original_image = original_image.squeeze(0)
            image = original_image.permute(2, 0, 1).to(device)

            semantic_mask, instance_mask = masks
            semantic_mask = semantic_mask.squeeze(0).to(device)
            instance_mask = instance_mask.squeeze(0).to(device)
            img_height, img_width = image.shape[-2:]
            pred_panoptic_tensor = torch.zeros(
                (img_height, img_width, 2), dtype=torch.long, device=device
            )

            inputs = [{"image": image, "height": img_height, "width": img_width}]
            pred_segmentation_map, segments_info = model(inputs)[0]["panoptic_seg"]

            next_instance_id = 1
            for segment_info in segments_info:
                segment_id = segment_info["id"]
                category_id = segment_info["category_id"]
                is_coco_thing = segment_info["isthing"]

                coco_label = (
                    thing_classes[category_id]
                    if is_coco_thing
                    else stuff_classes[category_id]
                )
                waymo_class_id = mappings.get_waymo_class_id_from_coco_label(coco_label)
                mask = pred_segmentation_map == segment_id

                is_waymo_thing = mappings.is_waymo_thing(waymo_class_id)
                instance_id = next_instance_id if is_waymo_thing else 0
                if is_waymo_thing:
                    next_instance_id += 1

                pred_panoptic_tensor[..., 0][mask] = waymo_class_id
                pred_panoptic_tensor[..., 1][mask] = instance_id

            target_panoptic_tensor = torch.stack(
                (semantic_mask, instance_mask),
                dim=-1,
            ).to(torch.long).unsqueeze(0)
            pred_panoptic_tensor = pred_panoptic_tensor.unsqueeze(0)

            pq_metric_avg.update(pred_panoptic_tensor, target_panoptic_tensor)
            pq_metric_per_class.update(pred_panoptic_tensor, target_panoptic_tensor)

    end_time = time.time()
    duration_in_seconds = end_time - start_time

    pq_results_avg = pq_metric_avg.compute()
    pq_results_per_class = pq_metric_per_class.compute()

    pq_avg = f"{pq_results_avg[0].item():.4f}"
    sq_avg = f"{pq_results_avg[1].item():.4f}"
    rq_avg = f"{pq_results_avg[2].item():.4f}"

    results = {
        "duration_in_seconds": duration_in_seconds,
        "metrics_avg": {
            "pq": pq_avg,
            "sq": sq_avg,
            "rq": rq_avg,
        },
        "metrics_per_class": [],
    }

    class_count = pq_results_per_class.shape[0]
    for i in range(class_count):
        class_metrics = pq_results_per_class[i]
        class_id = mappings.WAYMO_CONTINUOUS_IDS[i]
        class_label = mappings.WAYMO_CLASS_LABELS[class_id]
        class_results = {
            "class_label": class_label,
            "pq": f"{class_metrics[0].item():.4f}",
            "sq": f"{class_metrics[1].item():.4f}",
            "rq": f"{class_metrics[2].item():.4f}",
        }
        results["metrics_per_class"].append(class_results)

    pprint(results)


if __name__ == "__main__":
    evaluate_panopticfpn(
        waymo_data_dir=Path(
            os.environ.get("WAYMO_DATA_DIR", Path(__file__).parents[3] / "waymo_data")
        )
    )
