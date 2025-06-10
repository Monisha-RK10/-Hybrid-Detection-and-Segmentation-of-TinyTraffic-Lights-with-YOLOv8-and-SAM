# Evaluation Pipeline for YOLO seg & SAM

| Step                  | Process                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Annotation Format** | Started with Makesense.ai JSON containing **polygon masks**                         |
| **Label Conversion**  | Converted JSON to **YOLO segmentation `.txt` labels** (class\_id x1 y1 x2 y2 ...)   |
| **Training**          | Trained using `!yolo task=segment ...` with `data.yaml` (val + train folders)       |
| **Evaluation**        | - Automatically handled by Ultralytics during training (per-epoch val mAP, IoU) <br> No need for `pycocotools`, no manual binary masks, no custom IoU |
| **Model Output**      | Predictions are in **polygon format** (saved in `runs/segment/exp/`)                |

