## Dataset YAML Files

- `train.yaml` – Full Bosch Small Traffic Lights dataset used for earlier exploration.
- `curated_images.csv` — Handpicked image metadata for quality assurance.
- `data.yaml (for YOLOv8 detector)` – Curated subset used for training and evaluation.
- `data.yaml (for YOLOv8n/s segmenter)` — Segmentation format config for YOLOv8.
- `json (from Makesense.ai)` — Ground truth masks used for YOLOv8 segmentation.

All ~650 curated training images were manually selected from different Bosch folders and consolidated under images/. A full list of selected filenames is available in curated_list.csv for reproducibility.

