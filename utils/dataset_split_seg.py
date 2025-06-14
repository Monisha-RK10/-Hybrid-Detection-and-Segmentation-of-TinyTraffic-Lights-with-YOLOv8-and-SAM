# Step 6: Train/val Split 

import os
import random
import shutil

# Base folder path
base_path = "/content/drive/MyDrive/TrafficSignal/segmentation_updated"

# Input directories
image_dir = os.path.join(base_path, "images/train")
label_dir = os.path.join(base_path, "labels/train")

# Output directories
# Images
train_img_out = os.path.join(base_path, "images/train")
val_img_out = os.path.join(base_path, "images/val")
# Labels
train_lbl_out = os.path.join(base_path, "labels/train")
val_lbl_out = os.path.join(base_path, "labels/val")

# Ensure dirs
os.makedirs(val_img_out, exist_ok=True)
os.makedirs(val_lbl_out, exist_ok=True)

# Get all image filenames
all_images = [f for f in os.listdir(image_dir) if f.endswith(".png")]
random.shuffle(all_images)

# Define 80/20 split
val_split = int(0.2 * len(all_images))
val_images = all_images[:val_split]

# Move validation images and corresponding labels
for img_name in val_images:
    label_name = img_name.replace(".png", ".txt")

    shutil.move(os.path.join(image_dir, img_name), os.path.join(val_img_out, img_name))
    shutil.move(os.path.join(label_dir, label_name), os.path.join(val_lbl_out, label_name))

print("Split complete!")
