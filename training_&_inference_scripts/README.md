# Main Training & Inference Scripts

This folder contains scripts for training and evaluating YOLOv8 and SAM models for both detection and segmentation tasks on the Bosch Small Traffic Lights dataset.

---

### `train_yolo.py`
Trains a YOLOv8 detection model on the curated dataset.

- Task: **Object Detection**
- Model: YOLOv8n 
- Requires: `input/data.yaml`, image-label folders

---

### `inference_and_export.py`
Performs inference using a trained YOLOv8 detection model and exports annotated results.

- Input: Trained `.pt` weights
- Output: Visualized predictions (with confidence scores and class labels)

---

### `train_yolov8n_seg.py`
Trains a **YOLOv8n-seg** model for segmentation using polygon masks.

- Task: **Segmentation**
- Model: YOLOv8n-seg.pt 
- Requires: `input/data.yaml` (Polygon .txt labels in YOLOv8-seg format), image-label folders

---

### `train_yolov8s_seg.py`
Same as above, but using the larger YOLOv8s-seg model.

---

### `evaluation_sam.py`
Evaluates the hybrid detection + segmentation pipeline using YOLOv8 and SAM (Segment Anything Model).

- Input: Trained YOLOv8 `.pt` weights, Bosch annotation JSON
- Process:
  - Runs detection using YOLOv8 to get bounding boxes
  - Computes center points from boxes
  - Feeds both boxes and points into SAM to predict masks
  - Computes IoU with ground-truth (GT) segmentation masks
- Output:
  - Mean IoU score
  - Match count based on IoU > 0.05
  - Terminal print summary for analysis

---

### `inference_and_export_sam.py`
Similar to above, but only for visualization
