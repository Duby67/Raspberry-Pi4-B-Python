from ultralytics import YOLO

model = YOLO("best.pt")
results = model.predict(source="Test2.mp4", save=True)
