# Number-Plate-Recognition-Using-Yolov8

## Dataset Preparation

1. **Annotation with CVAT:**
- Use the CVAT online tool to annotate the images for number plate detection.
- Export the annotations in a YOLO-compatible format for seamless integration with the YOLOv8 model.

2. **Organizing the Dataset:**
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

## Vehicle and License Plate Detection

- YOLOv8 is used to detect vehicles (cars, buses, trucks) and license plates in each frame.
- SORT Tracker: Vehicle detection results are passed to the SORT tracking algorithm to track vehicles across multiple frames.
- License Plate Assignment: License plates are detected and matched with the corresponding vehicle using bounding box coordinates.

## Data Interpolation and Missing Data Handling

- Bounding Box Interpolation: Missing bounding boxes for vehicles and license plates are interpolated using linear interpolation.
- SciPy Interpolation: The interp1d function from SciPy is used to fill gaps between frames, ensuring continuous tracking of vehicles and license plates.
- Data Output: The final results, including interpolated bounding boxes and license plate text, are saved to a CSV file.

## Visualization and Video Output

- OpenCV Visualization: Bounding boxes for vehicles and license plates are drawn on the video frames. License plate text and cropped license plate images are displayed near the detected vehicles.
- Video Export: The processed frames, with bounding boxes and license plate annotations, are exported as a new video using OpenCV's VideoWriter.
- Display License Plate: License plate numbers are placed above each corresponding vehicle, and the license plate crops are superimposed on the video frames for visual clarity.



## Video:

1. The Video used in this project can be downloaded using the following link: 

```
https://www.pexels.com/video/traffic-flow-in-the-highway-2103099/

```


## Commands to Setup Project on Local Machine

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dyavadi8769/Automatic-Number-Plate-Detection-Using-Yolov8.git
   cd Automatic-Number-Plate-Detection-Using-Yolov8

2.  **Create a virtual environment and activate it:**
    ```bash
    conda create -p env python==3.10 -y
    conda activate env/ 

3.  **Install the Required Dependecies:**
    ```bash
    pip install -r requirements.txt

4. **Run the main.py to generate test.csv :**
    ```bash
    python main.py

5. **Run add_missing_data.py to add the missing data:**
    ```bash
    python add_missing_data.py

6. **Visualize the data by running visualize.py and generating out.mp4:**
    ```bash
    python visualize.py


# Author:

```bash
Author: Sai Kiran Reddy Dyavadi
Role  : Data Scientist
Email : dyavadi324@gmail.com
```
