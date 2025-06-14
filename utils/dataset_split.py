# Step 2: Train/val/test Split
# This code splits the cleaned Bosch subset into train, val, and test sets.

import os
import random
import shutil

def main():
    # Base paths
    base_dir = '/content/drive/MyDrive/TrafficSignal'
    image_dir = os.path.join(base_dir, 'images')
    output_dirs = ['train', 'val', 'test']

    # Create folders
    for split in output_dirs:
        os.makedirs(os.path.join(base_dir, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(base_dir, split, 'labels'), exist_ok=True)

    # Collect all images
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.png'))]
    image_files.sort()
    random.seed(42)
    random.shuffle(image_files)

    # Compute splits
    n = len(image_files)
    train_split = int(0.7 * n)
    val_split = int(0.9 * n)

    splits = {
        'train': image_files[:train_split],
        'val': image_files[train_split:val_split],
        'test': image_files[val_split:]
    }

    # Copy images and labels
    for split, files in splits.items():
        for file in files:
            image_src = os.path.join(image_dir, file)
            label_src = os.path.join(image_dir, file.rsplit('.', 1)[0] + '.txt')           # split the string from right, max 1 time.

            image_dst = os.path.join(base_dir, split, 'images', file)
            label_dst = os.path.join(base_dir, split, 'labels', os.path.basename(label_src))

            if os.path.exists(image_src) and os.path.exists(label_src):
                shutil.copy(image_src, image_dst)
                shutil.copy(label_src, label_dst)
            else:
                print(f"Missing file: {file}, skipping...")

    print(" Dataset split complete!")

if __name__ == "__main__":
    main()
