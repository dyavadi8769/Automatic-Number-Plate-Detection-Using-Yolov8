# Number-Plate-Recognition-Using-Yolov8

## Dataset Preparation

1. **Annotation with CVAT:**
- Use the CVAT online tool to annotate the images for number plate detection.
- Export the annotations in a YOLO-compatible format for seamless integration with the YOLOv8 model.

2. **Annotation with CVAT:**
- Prepare the dataset directory structure with subfolders for training, validation, and testing images.

3. **Configuration File (config.yaml):**
- Update the config.yaml file to define the dataset paths and class names, specifying where the training, validation, and test data are located.

## Model Training:

1. **Model Setup:**
- Load the YOLOv8 model configuration and prepare it for training using the yolov8n.yaml file.

2. **Training Execution:**
- Train the model using the annotated dataset as defined in the config.yaml file. Specify the number of epochs and other training parameters.

3. **Command Line Interface:**

- Alternatively, run the training process via the command line interface to facilitate batch processing and reproducibility.

```
yolo detect train data=yolov8_trained_model\config.yaml model=yolov8n.yaml epochs=1

```
