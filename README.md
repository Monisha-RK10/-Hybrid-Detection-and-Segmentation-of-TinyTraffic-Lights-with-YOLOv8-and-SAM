# Hybrid Detection and Segmentation of Small Traffic Lights using YOLOv8 and SAM

Small traffic light detection project using YOLOv8 for detection and SAM for segmentation.

## Dataset
- **[BOSCH Dataset](https://hci.iwr.uni-heidelberg.de/content/bosch-small-traffic-lights-dataset)**
- Contains images and bounding boxes for traffic lights.


## Model Output (Detection via YOLOv8n)
| Model        | Precision |  Recall  | mAP@0.5  | mAP@0.5:0.95 | Notes                      |
|--------------|-----------|----------|----------|--------------|--------------------------- |
| Red          | 0.77      | 0.52     |  0.58    |  0.30        | Common false positive      |
| Green        | 0.83      | 0.70     |  0.73    |  0.38        | High recall & precision    |
| All          | 0.80      | 0.61     |  0.66    |  0.34        | Faster inference (≈149 FPS)|

## Model Output (Segmention via YOLOv8n/s)
| Model       | Params | GFLOPs | Box mAP50 | Box mAP50-95 | Mask mAP50 | Mask mAP50-95 |
| ----------- | ------ | ------ | --------- | ------------ | ---------- | ------------- |
| YOLOv8s-seg | 11.8M  | ~42    | 0.86      | 0.75         | 0.07       | 0.0125        |
| YOLOv8n-seg | 3.2M   | ~12    | 0.83      | 0.73         | 0.02       | 0.00747       |

Note: These results may also be affected by annotation quality. Precisely annotating small objects with pixel-wise accuracy is challenging and can impact segmentation metrics.

**Read the full article [here](https://medium.com/@monishatemp20/yolov8-for-small-object-detection-real-world-use-case-on-traffic-lights-f3bbe95c742d)**

## Sample Predictions for Detection (via YOLOv8n) & Segmentation (via SAM)

### Detection (YOLOv8n)
![YOLOv8 Result](results/green.jpg)
![YOLOv8 Result](results/red.jpg)
![YOLOv8 Result](results/mixed.jpg)

### Segmentation (SAM)
![SAM Result](results/segmentation_on_green.png)
![SAM Result](results/segmentation_on_red.png)
![SAM Result](results/segmentation_on_red_green.png)

### Detection (False positive)
![YOLOv8 Result](results/false_positive.jpg)
