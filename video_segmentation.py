import cv2
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Load scene detection results
def load_scene_detection_results(file_path):
    results = []
    with open(file_path, 'r') as f:
        for line in f:
            frame_id, scene_type, people_present = line.strip().split(',')
            results.append((int(frame_id), scene_type, people_present == 'True'))
    return results

# Segment video
def segment_video(video_path, results):
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    segments = {
        'indoor': [],
        'outdoor': [],
        'people_present': [],
        'no_people': []
    }

    def write_segment(start_frame, end_frame, category):
        start_time = start_frame / frame_rate
        end_time = end_frame / frame_rate
        output_path = f"output_videos/{category}_{start_frame}_{end_frame}.mp4"
        ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=output_path)
        segments[category].append(output_path)

    os.makedirs('output_videos', exist_ok=True)
    prev_frame_id = 0
    prev_scene = None
    prev_people_present = None

    for frame_id, scene_type, people_present in results:
        if prev_scene is not None:
            if frame_id - prev_frame_id > frame_rate * 30:  # If the gap between frames is large, close the previous segment
                write_segment(prev_frame_id, frame_id, prev_scene)
                if prev_people_present:
                    write_segment(prev_frame_id, frame_id, 'people_present')
                else:
                    write_segment(prev_frame_id, frame_id, 'no_people')
                prev_frame_id = frame_id
                prev_scene = scene_type
                prev_people_present = people_present
            else:
                prev_scene = scene_type
                prev_people_present = people_present
        else:
            prev_frame_id = frame_id
            prev_scene = scene_type
            prev_people_present = people_present

    # Write the last segment
    if prev_scene is not None:
        write_segment(prev_frame_id, frame_id, prev_scene)
        if prev_people_present:
            write_segment(prev_frame_id, frame_id, 'people_present')
        else:
            write_segment(prev_frame_id, frame_id, 'no_people')

    cap.release()
    return segments

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    results = load_scene_detection_results('scene_detection_results.txt')
    segments = segment_video(video_path, results)
    print("Video segmentation completed. Segments saved in the output_videos directory.")
