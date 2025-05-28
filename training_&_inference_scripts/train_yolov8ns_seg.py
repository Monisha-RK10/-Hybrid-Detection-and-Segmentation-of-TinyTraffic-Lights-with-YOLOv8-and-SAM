# Train YOLOv8ns segmenter model

from ultralytics import YOLO

!yolo task=segment mode=train model=yolov8ns-seg.pt \
    data=/content/drive/MyDrive/TrafficSignal/segmentation_updated/data.yaml \
    epochs=250 imgsz=640 save=True
