# Step 7: Load model & yaml to train the model.
# Train YOLOv8n segmenter model

from ultralytics import YOLO

!yolo task=segment mode=train model=yolov8n-seg.pt \
    data=/content/drive/MyDrive/TrafficSignal/segmentation_updated/data.yaml \
    epochs=250 imgsz=640 save=True
