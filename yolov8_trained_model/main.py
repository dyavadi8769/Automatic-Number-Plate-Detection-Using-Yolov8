from ultralytics import YOLO
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

# Load YOLOv8 model
model= YOLO('yolov8n.yaml', weights_only=True)

# Using the model

results=model.train(data="config.yaml",epochs=1) # train the model