import cv2
import requests
import os
import numpy as np


subscription_key = '69f459252861417ba53a09764e99d07a'
endpoint = 'https://cv-project3.cognitiveservices.azure.com/'


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

def classify_frame(frame):
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(analyze_url, headers=headers, data=img_encoded.tobytes())
    
    try:
        response.raise_for_status()
        analysis = response.json()
        indoor_outdoor = 'indoor' if 'indoor' in analysis.get('tags', []) else 'outdoor'
        people_present = any('person' in obj.get('object', '') for obj in analysis.get('objects', []))
        return indoor_outdoor, people_present
    except Exception as e:
        print(f"Error processing frame: {e}")
        return None, None

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
