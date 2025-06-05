import json
import os
from pathlib import Path

# Step 5: Generate YOLO segmentation labels for images.

# Paths
json_path = Path("/content/drive/MyDrive/TrafficSignal/segmentation_updated/annotation.json")
images_dir = Path("/content/drive/MyDrive/TrafficSignal/segmentation_updated/images/train")
labels_dir = Path("/content/drive/MyDrive/TrafficSignal/segmentation_updated/labels/train")
labels_dir.mkdir(parents=True, exist_ok=True)

# Load COCO JSON
with open(json_path, 'r') as f:
    coco = json.load(f)

# Create a mapping from image_id to file_name
image_id_to_filename = {img['id']: img['file_name'] for img in coco['images']}
# Create a mapping from image_id to image size (width, height)
image_id_to_size = {img['id']: (img['width'], img['height']) for img in coco['images']}

# Create annotation lists grouped by image_id
annotations_per_image = {} # Approach 2: Pre-group annotations: O(1) lookup per image (very fast), no repeated filtering/searching.
for ann in coco['annotations']:
    image_id = ann['image_id']
    annotations_per_image.setdefault(image_id, []).append(ann) # setdefault(k, v) checks if k exists in the dictionary, {1: [ann1, ann2],  2: [ann3],  3: [ann4, ann5, ann6],...}

# Map category_id to zero-based index if needed
categories = coco['categories']
category_id_map = {cat['id']: i for i, cat in enumerate(categories)}  # cat: each dictionary inside categories, for ex categories = [{"id": 2, "name": "Red"}, {"id": 5, "name": "Green"}] result: category_id_map = {2: 0, 5: 1}

# Convert annotations to YOLOv8 segmentation format
for image_id, file_name in image_id_to_filename.items():
    width, height = image_id_to_size[image_id] # (W, H) lookup
    annotations = annotations_per_image.get(image_id, []) # All anns for this image
    lines = []

    for ann in annotations:
        category_id = ann['category_id']
        class_id = category_id_map[category_id]  # Map to YOLO class ID
        segmentation = ann['segmentation'][0]  # Only one polygon expected, to avoid multiple disconnected part
        xs = segmentation[0::2] # splits the polygon list into X coordinates (every other value starting from index 0)
        ys = segmentation[1::2] # splits the polygon list into Y coordinates (every other value starting from index 1)

        # Compute bounding box (YOLO format)
        x_min, y_min = min(xs), min(ys)
        x_max, y_max = max(xs), max(ys)
        x_center = (x_min + x_max) / 2 / width
        y_center = (y_min + y_max) / 2 / height
        w = (x_max - x_min) / width
        h = (y_max - y_min) / height

        # Normalize segmentation points (Normalize COCO polygon to YOLO format)
        # if i % 2 == 0: means X coordinate (even indices), divide it by width.
        # if i % 2 != 0: means Y coordinate (odd indices), divide it by height.
        norm_seg = [str(round(x / width, 6)) if i % 2 == 0 else str(round(x / height, 6))
                    for i, x in enumerate(segmentation)] # Round to 6 decimal places, and convert to string 

        line = f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f} " + " ".join(norm_seg)
        lines.append(line)

    # Write label file
    label_file = labels_dir / (Path(file_name).stem + ".txt")
    with open(label_file, "w") as f:
        f.write("\n".join(lines))

labels_dir.exists(), len(list(labels_dir.glob("*.txt")))  # Return status and file count
