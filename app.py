import streamlit as st
import cv2
import os
from scene_detection import detect_scenes
from video_segmentation import segment_video

st.title("Video Segmentation Application")

uploaded_file = st.file_uploader("Choose a video file...", type=["mp4"])

if uploaded_file is not None:
    video_path = os.path.join("uploads", uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.write("Video uploaded successfully!")

    if st.button("Process Video"):
        results = detect_scenes(video_path)
        with open('scene_detection_results.txt', 'w') as f:
            for frame_id, scene_type, people_present in results:
                f.write(f"{frame_id},{scene_type},{people_present}\n")
        segments = segment_video(video_path, results)
        st.write("Video segmentation completed!")
        st.write("Segments saved in the output_videos directory.")
