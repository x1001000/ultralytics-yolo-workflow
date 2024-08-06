from ultralytics import YOLO
model = YOLO("/usr/src/ultralytics/runs/detect/train3/weights/best.pt")
model.export()