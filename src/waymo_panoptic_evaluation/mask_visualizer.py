import hashlib
from typing import Dict, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image

def _deterministic_color(label: int) -> Tuple[int, int, int]:
    h = hashlib.sha256(str(label).encode()).digest()
    return tuple(h[:3])

def colorize(
    mask: torch.Tensor,
    instance: Optional[torch.Tensor] = None,
    shared_label_map: Optional[Dict[int, Tuple[int, int, int]]] = None
) -> Image.Image:
    label_mask = mask.squeeze().cpu().numpy()

    if instance is not None:
        instance = instance.squeeze().cpu().numpy()
        label_mask = label_mask.astype(np.int32) * 1000 + instance.astype(np.int32)

    label_mask = label_mask.astype(np.uint32)
    unique_labels = np.unique(label_mask)

    if shared_label_map is None:
        shared_label_map = {label: _deterministic_color(label) for label in unique_labels}
    else:
        for label in unique_labels:
            if label not in shared_label_map:
                shared_label_map[label] = _deterministic_color(label)

    h, w = label_mask.shape
    color_img = np.zeros((h, w, 3), dtype=np.uint8)

    for label in unique_labels:
        color_img[label_mask == label] = shared_label_map[label]

    return Image.fromarray(color_img)

def visualize_masks(
    gt_sem: torch.Tensor,
    gt_inst: torch.Tensor,
    pred_sem: torch.Tensor
) -> None:
    gt_colored = colorize(gt_sem, gt_inst)
    pred_colored = colorize(pred_sem[..., 0], pred_sem[..., 1])

    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].imshow(gt_colored)
    axs[0].set_title("Ground Truth")
    axs[1].imshow(pred_colored)
    axs[1].set_title("Prediction")
    for ax in axs:
        ax.axis("off")
    plt.tight_layout()
    plt.show()