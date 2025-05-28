from ultralytics import YOLO

# Step 3: Load model & yaml to train the model.
# Train model by setting epoch, image size, batch size.

model = YOLO('yolov8n.yaml')  # or 'yolov8s.yaml'
model.train(data='/content/drive/MyDrive/TrafficSignal/data.yaml', epochs=100, patience=20,  imgsz=640, batch=16)
