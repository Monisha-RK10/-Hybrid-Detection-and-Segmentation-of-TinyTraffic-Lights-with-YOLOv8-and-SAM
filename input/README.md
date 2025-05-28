# input/

This folder contains dataset metadata, configuration files, and annotation references used for both detection and segmentation tasks in the traffic light project.

---

### Files

- **`train.yaml`**  
  Full Bosch Small Traffic Lights dataset used during initial exploration.

- **`curated_images.csv`**  
  List of ~650 handpicked images selected from different Bosch folders based on quality, visibility, and class balance.

- **`data.yaml`** (for YOLOv8 detector)  
  Dataset configuration for the curated subset used in detection training and evaluation.

- **`data.yaml`** (for YOLOv8n/s segmenter)  
  Dataset configuration in segmentation format for YOLOv8n and YOLOv8s training.

- **`annotations.json`** *(from MakeSense.ai)*  
  COCO-style polygon masks for ~100 manually annotated images, used as ground truth for YOLOv8 segmentation.

---

### Notes

- All curated images are consolidated under `images/` for simplified access.
- The `curated_images.csv` ensures full reproducibility of the dataset split.
- Segmentation annotations were created using [MakeSense.ai](https://www.makesense.ai/) and follow the COCO format structure.

