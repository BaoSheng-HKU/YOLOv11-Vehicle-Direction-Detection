"""
Example: Using a YOLOv11 model to perform direction detection (e.g., front/rear) on a full image.

Requirements:
- ultralytics library (YOLOv11 support)
- A trained YOLOv11 model for direction detection
- OpenCV (cv2) for image handling

Output:
- Saves an image with detection boxes and direction labels to the specified directory.
"""

import os
import cv2
from ultralytics import YOLO

# ===== 1. Setup parameters =====
image_path = "path/to/your/XX.jpg"        # ToDo: Replace with the path to your input frame
output_dir = "path/to/save/output/results"   # ToDo: Replace with your desired output directory
os.makedirs(output_dir, exist_ok=True)

# ===== 2. Load the trained direction detection model =====
model_direction = YOLO("path/to/your/best.pt")  # ToDo: Replace with the path to the trained YOLOv11 model

# ===== 3. Read the image =====
frame = cv2.imread(image_path)
if frame is None:
    raise FileNotFoundError(f"Image not found: {image_path}")

# Optional: create a copy for drawing
frame_cp = frame.copy()

# ===== 4. Run direction detection =====
results = model_direction(frame_cp, agnostic_nms=True)

# ===== 5. Visualize and save the result =====
for i, r in enumerate(results):
    annotated_img = r.plot()  # Draws boxes and labels on the image
    out_path = os.path.join(output_dir, "direction_result.jpg")
    cv2.imwrite(out_path, annotated_img)
    print(f"Saved detection result to: {out_path}")
