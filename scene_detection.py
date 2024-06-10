import cv2
import requests
import os
import numpy as np

# Azure Computer Vision API setup
subscription_key = 'YOUR_AZURE_SUBSCRIPTION_KEY'
endpoint = 'YOUR_AZURE_ENDPOINT_URL'
analyze_url = endpoint + "vision/v3.1/analyze"

# Frame extraction function
def extract_frames(video_path, interval=30):
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frames = []
    frame_id = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % (frame_rate * interval) == 0:
            frames.append((frame_id, frame))
        frame_id += 1
    cap.release()
    return frames

# Scene classification function
def classify_frame(frame):
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(analyze_url, headers=headers, data=img_encoded.tobytes())
    response.raise_for_status()
    analysis = response.json()
    indoor_outdoor = 'indoor' if 'indoor' in analysis['tags'] else 'outdoor'
    people_present = any('person' in obj['object'] for obj in analysis['objects'])
    return indoor_outdoor, people_present

# Main function
def detect_scenes(video_path):
    frames = extract_frames(video_path)
    results = []
    for frame_id, frame in frames:
        try:
            scene_type, people_present = classify_frame(frame)
            results.append((frame_id, scene_type, people_present))
        except Exception as e:
            print(f"Error processing frame {frame_id}: {e}")
    return results

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    results = detect_scenes(video_path)
    with open('scene_detection_results.txt', 'w') as f:
        for frame_id, scene_type, people_present in results:
            f.write(f"{frame_id},{scene_type},{people_present}\n")
    print("Scene detection completed. Results saved to scene_detection_results.txt.")
