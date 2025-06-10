# Evaluation Pipeline for YOLO seg & SAM

## YOLOv8 Segmentation Pipeline Summary

| Step                  | Process                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Annotation Format** | Started with Makesense.ai JSON containing **polygon masks**                         |
| **Label Conversion**  | Converted JSON to **YOLO segmentation `.txt` labels** (class\_id x1 y1 x2 y2 ...)   |
| **Training**          | Trained using `!yolo task=segment ...` with `data.yaml` (val + train folders)       |
| **Evaluation**        | - Automatically handled by Ultralytics during training (per-epoch val mAP, IoU) <br> - No need for `pycocotools`, no manual binary masks, no custom IoU |
| **Model Output**      | Predictions are in **polygon format** (saved in `runs/segment/exp/`)                |

## SAM + Evaluation Pipeline Summary

| Step                  | Process                 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **No Training**       | Just used **inference** with `predictor.predict(...)`                           |
| **Prediction Output** | SAM gives **binary masks** directly (numpy arrays, shape H×W, values {0,1})     |
| **GT Annotations**    | Used **same Makesense.ai JSON** but passed it through `pycocotools` to: <br> - Extract polygons <br> - Convert to **binary masks** (via `frPyObjects` → `merge` → `decode`) |
| **Evaluation**        | Manually computed **IoU = intersection / union** between: <br> - `pred_mask` (from SAM) <br> - `gt_mask` (from pycocotools conversion)       |
| **No model.eval()**   | Because SAM wasn't trained, it was just used for point/box-based inference                                                            |
