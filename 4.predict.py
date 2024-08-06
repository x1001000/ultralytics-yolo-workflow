from ultralytics import YOLO
model = YOLO("/usr/src/ultralytics/runs/detect/train/weights/best.pt")

import glob
tests = sorted(glob.glob("valid/images/*.jpg"))[:2]
results = model(tests)

for test, result in zip(tests, results):
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    # result.show()  # display to screen
    result.save(filename=f"{test.split('/')[2].split('_jpg')[0]}.jpg")  # save to disk