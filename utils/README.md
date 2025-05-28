# utils/

Utility scripts to preprocess data and generate YOLOv8-compatible annotations for both detection and segmentation tasks.

---

### `dataset_split.py`
Splits the detection dataset into **70% training**, **20% validation**, and **10% testing** by moving images and labels into corresponding folders.

### `dataset_split_seg.py`
Splits the segmentation dataset (image and polygon-label pairs) into **80% training** and **20% validation** folders.

### `yolo_label_gen.py`
Converts Bosch `train.yaml` annotations into YOLOv8 format for selected images (used for object detection).
- **Input**: `images/`, `train.yaml` (from Bosch dataset)
- **Output**: YOLOv8 `.txt` labels with class and bounding box

### `yolo_seg_label_gen.py`
Converts COCO-style segmentation annotations into YOLOv8 format (used for polygon-based segmentation).
- **Input**: `images/`, `annotations.json` (from MakeSense.ai)
- **Output**: YOLOv8 `.txt` segmentation labels with polygon points

---

### Note
Make sure to update file paths inside each script before running.

Each script assumes the following folder structure:

TrafficSignal/

├── images/

│ ├── train/

│ └── val/

├── labels/

│ ├── train/

│ └── val/

├── annotations.json # or train.yaml for Bosch
