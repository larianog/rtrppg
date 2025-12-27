import os
import numpy as np
import cv2

def main_exp():
    current_path = os.getcwd()
    video_path = os.path.join(current_path, "video/pilot.mp4")
    dataset_path = os.path.join(current_path, "demo_subject/example")

    create_dataset(video_path, dataset_path)

def create_dataset(video_path, dataset_path):
    """
    Creates a new dataset with the timestamp file, and the frames converted to a numpy array.
    
    Args:
        video_path (str): The file path to the .mp4 file.
        dataset_path (str): The dataset path in which the files will be saved.
    """

    if not os.path.isdir(dataset_path):
        os.mkdir(dataset_path)
        print(f"Created a new folder at {dataset_path}")

    save_video_to_numpy(video_path, dataset_path)
    extract_video_timestamps(video_path, dataset_path)
    
    print(f"Successfully saved video")


def extract_video_timestamps(video_path, dataset_path):
    """
    Opens a video file, reads each frame into a NumPy array, 
    and extracts the timestamp information for each frame.
    """
    print(f"Attempting to open video file: {video_path}")

    # 1. Open the video file using OpenCV's VideoCapture object
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_path}'. Please check the path and file permissions.")
        return

    # Get some properties of the video stream
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_seconds = frame_count / fps if fps > 0 else 0

    print(f"Video properties: FPS={fps:.2f}, Frame Count={frame_count}, Duration={duration_seconds:.2f}s")
    print("-" * 40)

    frame_data = [] # To store strings of timestamp
    frame_number = 0

    # 2. Loop through the video frames
    while True:
        # Read a frame (ret is a boolean, frame is a NumPy array)
        ret, _ = cap.read()

        # Check if the frame was read successfully (end of video reached?)
        if not ret:
            break

        # 3. Extract the timestamp information
        current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        current_time_s = current_time_ms * 10**(-3)

        # Store or process your data
        frame_data.append(f"{current_time_s:.18e}")
        frame_number += 1

    # 4. Release the video capture object and close all windows
    cap.release()
    # cv2.destroyAllWindows()

    print("-" * 40)
    print(f"Finished processing {len(frame_data)} frames.")

    filename = "example_timestamp.txt"
    filepath = os.path.join(dataset_path, f"{dataset_path}/{filename}")

    with open(filepath, "w") as file_handle:
        # Ensure all elements are strings first (using a generator expression)
        data_to_write = '\n'.join(str(item) for item in frame_data)
        file_handle.write(data_to_write)

    return frame_data

def save_video_to_numpy(video_path, dataset_path):
    """
    Resizes image to square size of size sqr_size
    
    Saves an MP4 video file into a 4D numpy array file using OpenCV.

    Args:
        video_path (str): The file path to the .mp4 file.

    """
    if not os.path.exists(video_path):
        print(f"Error: File not found at {video_path}")
        return None

    frames = []
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None

    print(f"Loading video: {video_path}")

    new_dimensions = (8,8)
    
    ret = True
    while ret:
        ret, frame = cap.read() # Read one frame
        if ret:
            # OpenCV reads frames in BGR format by default. 
            # If you need RGB, convert it:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resized_image = cv2.resize(frame_rgb, new_dimensions, interpolation=cv2.INTER_AREA)

            frames.append(resized_image)
    
    cap.release() # Release the VideoCapture object
    
    # Stack the list of 3D frame arrays into a single 4D array
    video_array = np.stack(frames, axis=0)
    np.save(os.path.join(dataset_path, "example"), video_array) 
    
    print(f"Successfully saved video")

if __name__ == "__main__":
    main_exp()