# Scene-Based Video Segmentation

This project segments a video into four categories based on scenes and the presence of people:
1. Indoor scenes
2. Outdoor scenes
3. Scenes with people present
4. Scenes without people present

The segmentation is performed using Azure Cognitive Services for scene classification and object detection, OpenCV for video processing, and Streamlit for creating a user-friendly interface.

## Prerequisites

- Python 3.6 or higher
- Azure Cognitive Services account with subscription key and endpoint URL
- Required libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NikitanikiJB/object-detection.git
    cd object-detection
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Running the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2. **Uploading and processing a video**:
    - Open the URL provided by Streamlit in your browser (usually `http://localhost:8501`).
    - Upload a video file.
    - The application will process the video and display the segmented clips.

## File Structure

- `scene_detection.py`: Contains the logic for scene detection.
- `app.py`: Streamlit application for uploading videos and displaying results.
- `requirements.txt`: List of required Python libraries.
- `scene_detection.py`: Contains the logic for video segmentation.


