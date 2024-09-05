from ultralytics import YOLO
import cv2

coco_model=YOLO('yolov8n.pt')
license_plate_detector= YOLO("license_plate_detector.pt")
