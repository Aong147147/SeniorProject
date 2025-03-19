# record_frame.py
import os
import cv2

def setup_frame_savers(output_folder):
    # os.makedirs(output_folder, exist_ok=True)
    rgb_folder = os.path.join(output_folder, "rgb_frames")
    depth_folder = os.path.join(output_folder, "depth_frames")
    rgb_no_label_folder = os.path.join(output_folder, "rgb_no_label_frames")
    
    
    return rgb_folder, depth_folder, rgb_no_label_folder

def save_frame(frame, folder, frame_index):
    
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    
    frame_path = os.path.join(folder, f"frame_{frame_index:04d}.png")
    
    success = cv2.imwrite(frame_path, frame)
    if not success:
        print(f"Failed to save frame at {frame_path}")
    else:
        print(f"Frame saved successfully at {frame_path}")

