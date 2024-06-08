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
    git clone https://github.com/your-repo/video-segmentation.git
    cd video-segmentation
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Azure Cognitive Services**:
    - Create an Azure Cognitive Services resource and get the subscription key and endpoint URL.
    - Update `scene_detection.py` with your Azure subscription key and endpoint.

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

- `scene_detection.py`: Contains the logic for scene detection and video segmentation.
- `app.py`: Streamlit application for uploading videos and displaying results.
- `requirements.txt`: List of required Python libraries.

## Approach

- **Objective**: To segment a video based on indoor/outdoor scenes and the presence of people.
- **Tools Used**:
  - Azure Cognitive Services for scene classification and object detection.
  - OpenCV and MoviePy for video processing.
  - Streamlit for creating a user-friendly interface.

## Implementation Steps

1. **Set up Azure Cognitive Services**: Created a Cognitive Services resource and obtained the subscription key and endpoint.
2. **Scene Detection**:
   - Extracted frames from the video using OpenCV.
   - Analyzed each frame using the Azure Computer Vision API to classify scenes and detect people.
3. **Video Segmentation**:
   - Segmented the video into different categories (indoor, outdoor, people present, people not present) based on the analysis.
   - Used MoviePy to create and save video clips for each category.
4. **Streamlit UI**:
   - Created a Streamlit application to allow users to upload videos and view segmented clips.

## Challenges Faced

- **Integration with Azure Cognitive Services**: Ensuring that the API requests were correctly formatted and handled.
- **Performance**: Processing video frames can be slow, especially for longer videos.
- **Accuracy**: Ensuring that the scene classification and people detection were accurate.

## Solutions Implemented

- **Optimized API Calls**: Reduced the number of API calls by analyzing key frames instead of every frame.
- **Improved Segmentation Logic**: Refined the logic for segmenting video based on the classification results to improve accuracy.
- **Streamlined User Interface**: Made the Streamlit application user-friendly and easy to use.

## Potential Improvements

- **Batch Processing**: Implement batch processing of frames to improve performance.
- **Advanced Classification**: Use more advanced models for scene classification and people detection.
- **Enhanced UI**: Add more features to the Streamlit application, such as the ability to download segmented clips.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)
- [OpenCV](https://opencv.org/)
- [MoviePy](https://zulko.github.io/moviepy/)
- [Streamlit](https://streamlit.io/)
