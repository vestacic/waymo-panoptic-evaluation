#!/bin/bash

INPUT_IMAGES_DIR="$HOME/waymo_data/raw_images_temp"
INPUT_SEGMENTATIONS_DIR="$HOME/waymo_data/segmentations_temp"
PROCESSING_IMAGES_DIR="$HOME/waymo_data/raw_images"
PROCESSING_SEGMENTATIONS_DIR="$HOME/waymo_data/segmentations"
DONE_IMAGES_DIR="$HOME/waymo_data/images_processed"
DONE_SEGMENTATIONS_DIR="$HOME/waymo_data/segmentations_processed"
PYTHON_SCRIPT="$HOME/src/waymo_panoptic_evaluation/waymo_reader.py"

mkdir -p "$PROCESSING_IMAGES_DIR" "$PROCESSING_SEGMENTATIONS_DIR" "$DONE_IMAGES_DIR" "$DONE_SEGMENTATIONS_DIR"

for FILE in "$INPUT_IMAGES_DIR"/*; do
    [ -e "$FILE" ] || continue

    BASENAME=$(basename "$FILE")

    echo "Processing: $BASENAME"

    mv "$INPUT_IMAGES_DIR/$BASENAME" "$PROCESSING_IMAGES_DIR/$BASENAME"
    mv "$INPUT_SEGMENTATIONS_DIR/$BASENAME" "$PROCESSING_SEGMENTATIONS_DIR/$BASENAME"

    python3 "$PYTHON_SCRIPT"

    mv "$PROCESSING_IMAGES_DIR/$BASENAME" "$DONE_IMAGES_DIR/$BASENAME"
    mv "$PROCESSING_SEGMENTATIONS_DIR/$BASENAME" "$DONE_SEGMENTATIONS_DIR/$BASENAME"

    echo "Finished: $BASENAME"
done
