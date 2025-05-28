# utils/

Utility scripts to preprocess data and generate YOLOv8-compatible annotations for both detection and segmentation tasks.

### `dataset_split.py`
Splits detection dataset into 20% training, 20% validation and 10% testing by moving images and labels into corresponding folders.

### `dataset_split_seg.py`
Splits segmentation dataset (image and polygon-label pairs) into 80% training and 20% validation folders.

### `yolo_label_gen.py`
Converts Bosch annotations (`train.yaml`) into YOLOv8 format for selected images for object detection.
- Input: `images/`, `train.yaml` (from Bosch dataset)
- Output: YOLOv8 `.txt` labels with class and bounding box

### `yolo_seg_label_gen.py`
Converts COCO-style segmentation annotations into YOLOv8 format for selected images for segmentation (polygon masks).
- Input: `images/`, `annotations.json` (from MakeSense AI)
- Output: YOLOv8 segmentation `.txt` labels with polygon points

---

Make sure to update `paths` inside each script before running. 

├── images/

│ ├── train/

│ └── val/

├── labels/

│ ├── train/

│ └── val/

├── annotation.json
