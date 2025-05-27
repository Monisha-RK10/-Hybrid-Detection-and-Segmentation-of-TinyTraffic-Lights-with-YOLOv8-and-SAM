from ultralytics import YOLO
from google.colab import files

# Step 4: Load model & run prediction

model = YOLO("/content/drive/MyDrive/TrafficSignal/best.pt")
results = model.predict(source="/content/drive/MyDrive/TrafficSignal/test/images", save=True, conf=0.25)

# Step 5: Zip & download results

!zip -r results.zip runs/detect/predict/
files.download("results.zip")

# Step 6: Export for deployment

model.export(format="onnx")
files.download("best.onnx")
