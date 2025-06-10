from ultralytics import YOLO
from pycocotools.coco import COCO
import numpy as np
import cv2
import os
from tqdm import tqdm
from segment_anything import sam_model_registry, SamPredictor

# Step 10: Evaluate trained YOLOv8 and SAM models by computing IoU between GT (MakeSenseAI) and predicted masks
# by guiding SAM with image,boxes (labels), centers obtained by YOLOv8 model.

# Load json, images, pre-trained (YOLO+SAM) models.
annotation_file = "/content/drive/MyDrive/TrafficSignal/segmentation_updated/annotation.json"
train_dir = "/content/drive/MyDrive/TrafficSignal/makesense"
yolo_model = YOLO("/content/drive/MyDrive/TrafficSignal/best_100_patience_20.pt")
sam_checkpoint = "/content/sam_vit_b_01ec64.pth"
sam = sam_model_registry["vit_b"](checkpoint=sam_checkpoint)
predictor = SamPredictor(sam)

# Open annotation file in COCO format and get image ids.
coco = COCO(annotation_file)
image_ids = coco.getImgIds()

# Initialize IoUs, matches, total GTs to keep track.
total_ious = []
matched = 0
total_gt = 0

# This function returns center for xyxy.
def get_center_point(box):
    x1, y1, x2, y2 = box
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    return cx, cy

# Loop through all the image ids to get image path. Perform detection on that image (xyxy) via YOLO. Extract center & boxes to guide SAM.
# For each image ID, get all annotations. For each annotation, get segmentation field. Convert polygon format to RLE to binary mask. Perform IoU between GT & predicted masks.
for img_id in tqdm(image_ids):
    img_info = coco.loadImgs(img_id)[0]
    img_path = os.path.join(train_dir, img_info['file_name'])  # Adjust for train_dir if needed
    image = cv2.imread(img_path)
    if image is None:
        continue

    # Predictions
    detections = yolo_model(img_path)[0].boxes.xyxy.cpu().numpy() # tensor([[124.2, 64.8, 192.7, 108.3]]) ->  [[124, 64, 192, 108]]
    predictor.set_image(image)
    for det_box in detections:
        x1, y1, x2, y2 = map(int, det_box)
        cx, cy = get_center_point([x1, y1, x2, y2])

        input_box = np.array([x1, y1, x2, y2]) # shape: (4,)
        input_point = np.array([[cx, cy]])
        input_label = np.array([1])  # foreground

        masks, scores, _ = predictor.predict(
            point_coords=input_point,
            point_labels=input_label,
            box=input_box[None, :],  # shape: (1, 4)
            multimask_output=False
        )
        pred_mask = masks[0]                                                      # For each predicted mask:

        # GT masks
        image_shape = image.shape[:2]
        gt_anns = coco.loadAnns(coco.getAnnIds(imgIds=img_id))                    # Approach 1: search the big annotation list every time (via getAnnIds): clean and readable, speed isn't a concern.

        for ann in gt_anns:                                                       # Loop over all GT masks
            gt_poly = ann['segmentation']                                         # list of polygons
            rle = mask_utils.frPyObjects(gt_poly, image_shape[0], image_shape[1]) # converts each polygon to RLE (Run-Length Encoding)
            rle = mask_utils.merge(rle)                                           # merges multiple polygons into one RLE mask
            gt_mask = mask_utils.decode(rle)                                      # converts that RLE into a binary mask, the above three steps are taken care in COCOeval (GT conversion from polygon to binary behind the scenes).

            intersection = np.logical_and(pred_mask, gt_mask).sum()
            union = np.logical_or(pred_mask, gt_mask).sum()
            if union > 0:
                iou = intersection / union                                        
                total_ious.append(iou)
                if iou > 0.05:
                    matched += 1                                                  
                total_gt += 1

mean_iou = np.mean(total_ious) if total_ious else 0
print(f"===== SAM Mask Evaluation with Center Point Prompt =====")
print(f"Total GT Objects Evaluated: {total_gt}")
print(f"Matched (IoU > 0.05): {matched} / {total_gt}")
print(f"Mean IoU: {mean_iou:.4f}")
