import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from waymo_panoptic_evaluation.mappings import WAYMO_CLASS_LABELS

ID_TO_COLOR = {
    0: None,
    1: "black",
    2: "yellow",
    3: "blue",
    4: "dodgerblue",
    5: "purple",
    6: "cyan",
    7: "darkviolet",
    8: "turquoise",
    9: "red",
    10: "orange",
    11: "orangered",
    12: "lightgoldenrodyellow",
    13: "saddlebrown",
    14: "darkorange",
    15: "navy",
    16: "hotpink",
    17: "gold",
    18: "lime",
    19: "chocolate",
    20: "gray",
    21: "white",
    22: "lightgray",
    23: "deeppink",
    24: "limegreen",
    25: "deepskyblue",
    26: "navajowhite",
    27: "magenta",
    28: "mediumseagreen",
}

def plot_image(
    image,
    instance_mask,
    semantic_mask
):
    image_height, image_width = image.shape[:2]
    
    _, ax = plt.subplots(1, figsize=(12, 9))
    ax.imshow(image)
    ax.axis("off")

    drawn_semantic_ids = []
    unique_instance_ids = np.unique(instance_mask)
    instance_ids = unique_instance_ids[unique_instance_ids != 0]
    
    for instance_id in instance_ids:
        instance_binary_mask = instance_mask == instance_id

        semantic_ids_in_instance = semantic_mask[instance_binary_mask]

        counts = np.bincount(semantic_ids_in_instance)
        semantic_id = np.argmax(counts)
        drawn_semantic_ids.append(semantic_id)
        
        semantic_type_name = WAYMO_CLASS_LABELS[semantic_id]

        mask_color_name = ID_TO_COLOR[semantic_id]

        rgba_color = mcolors.to_rgba(mask_color_name, alpha=0.5)

        mask_overlay = np.zeros((image_height, image_width, 4), dtype=np.uint8)

        mask_overlay[instance_binary_mask, :3] = (
            np.array(rgba_color[:3]) * 255
        ).astype(np.uint8)
        mask_overlay[instance_binary_mask, 3] = int(rgba_color[3] * 255)

        ax.imshow(mask_overlay)

        y_coords, x_coords = np.where(instance_binary_mask)

        if len(x_coords) > 0 and len(y_coords) > 0:
            text_x = int(np.mean(x_coords))
            text_y = int(np.mean(y_coords))

            text_x = np.clip(text_x, 0, image_width - 1)
            text_y = np.clip(text_y, 10, image_height - 1)

            ax.text(
                text_x,
                text_y,
                f"{semantic_type_name} ({instance_id})",
                color="white",
                fontsize=7,
                weight="bold",
                bbox=dict(
                    facecolor=mask_color_name,
                    alpha=0.7,
                    pad=1,
                    edgecolor="none",
                ),
            )
    
    unique_semantic_ids = np.unique(semantic_mask)
    semantic_ids = unique_semantic_ids[unique_semantic_ids != 0]
    for semantic_id in semantic_ids:
        if semantic_id in drawn_semantic_ids:
            continue
        
        semantic_mask_bin = semantic_mask == semantic_id        
        semantic_type_name = WAYMO_CLASS_LABELS[semantic_id]

        mask_color_name = ID_TO_COLOR[semantic_id]

        rgba_color = mcolors.to_rgba(mask_color_name, alpha=0.5)

        mask_overlay = np.zeros((image_height, image_width, 4), dtype=np.uint8)

        mask_overlay[semantic_mask_bin, :3] = (
            np.array(rgba_color[:3]) * 255
        ).astype(np.uint8)
        mask_overlay[semantic_mask_bin, 3] = int(rgba_color[3] * 255)

        ax.imshow(mask_overlay)

        y_coords, x_coords = np.where(semantic_mask_bin)

        if len(x_coords) > 0 and len(y_coords) > 0:
            text_x = int(np.mean(x_coords))
            text_y = int(np.mean(y_coords))

            text_x = np.clip(text_x, 0, image_width - 1)
            text_y = np.clip(text_y, 10, image_height - 1)

            ax.text(
                text_x,
                text_y,
                f"{semantic_type_name}",
                color="white",
                fontsize=7,
                weight="bold",
                bbox=dict(
                    facecolor=mask_color_name,
                    alpha=0.7,
                    pad=1,
                    edgecolor="none",
                ),
            )

    plt.show()