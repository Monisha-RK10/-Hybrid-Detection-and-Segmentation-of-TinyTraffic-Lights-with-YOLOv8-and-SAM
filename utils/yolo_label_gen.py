import yaml
import os
from PIL import Image

# Step 1: Generate YOLO labels for images.
# This piece of code generates labels for the selected subset of clean images.
# Labels are extracted from the train.yaml with the help of image name (Bosch dataset follows global name).
# Import necessary libraries.

# Helper function to map labels to YOLO classes
def map_label(label):
    if label.startswith('Red'):
        return 0
    elif label.startswith('Green'):
        return 1
    # elif label.startswith('Yellow'):
    #     return 2  # Optional
    else:
        return None  # Skip 'Off' and others

def main():
    # Paths
    image_dir = '/content/drive/MyDrive/TrafficSignal/images'
    yaml_path = '/content/drive/MyDrive/TrafficSignal/train.yaml'

    # Load YAML
    with open(yaml_path, 'r') as f:
        bosch_data = yaml.safe_load(f) # loads basic Python objects (like dict, list, str, int)

    # Track stats
    num_found = 0
    num_missing = 0

    for image_file in os.listdir(image_dir):
        if not image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        full_image_path = os.path.join(image_dir, image_file)

        # Get image dimensions
        try:
            with Image.open(full_image_path) as img:
                img_w, img_h = img.size
        except:
            print(f"Could not open image: {image_file}")
            continue

        # Find matching entry in YAML
        found = False
        for entry in bosch_data:
            if os.path.basename(entry['path']) == image_file:

                label_path = full_image_path.replace('.png', '.txt').replace('.jpg', '.txt').replace('.jpeg', '.txt')

                with open(label_path, 'w') as out:
                    for box in entry['boxes']:
                        cls = map_label(box['label']) # Call the function 'map_label'
                        if cls is None:
                            continue

                        x_min = box['x_min']
                        y_min = box['y_min']
                        x_max = box['x_max']
                        y_max = box['y_max']

                        # Convert to YOLO format
                        x_center = ((x_min + x_max) / 2) / img_w
                        y_center = ((y_min + y_max) / 2) / img_h
                        box_w = (x_max - x_min) / img_w
                        box_h = (y_max - y_min) / img_h

                        out.write(f"{cls} {x_center:.6f} {y_center:.6f} {box_w:.6f} {box_h:.6f}\n") # 6 decimal places (standard in YOLO label files)

                num_found += 1
                found = True
                break

        if not found:
            num_missing += 1

    print(f"Generated YOLO labels for {num_found} images.")
    print(f"Skipped {num_missing} images (no annotations).")

if __name__ == "__main__":
    main()
