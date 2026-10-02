"""
AI-Based Intelligent Traffic Light Manager

Day 2:
OpenCV Video Processing Module
"""

import cv2
import time


VIDEO_PATH = "videos/traffic.mp4"


def process_video():
    # Open traffic video
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("ERROR: Could not open traffic video.")
        print(f"Check that the file exists: {VIDEO_PATH}")
        return

    # Get video information
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("=" * 50)
    print("AI TRAFFIC LIGHT MANAGER")
    print("DAY 2 - OPENCV VIDEO PROCESSING")
    print("=" * 50)

    print(f"Video FPS       : {fps:.2f}")
    print(f"Video Resolution: {width} x {height}")
    print(f"Total Frames    : {total_frames}")
    print("=" * 50)

    frame_number = 0
    start_time = time.time()

    while True:
        # Read one frame
        ret, frame = cap.read()

        if not ret:
            break

        frame_number += 1

        # Resize frame for processing/display
        display_frame = cv2.resize(frame, (960, 540))

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        if elapsed_time > 0:
            current_fps = frame_number / elapsed_time
        else:
            current_fps = 0

        # Display information on video
        cv2.putText(
            display_frame,
            f"Frame: {frame_number}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            display_frame,
            f"FPS: {current_fps:.2f}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            display_frame,
            "Day 2 - OpenCV Video Processing",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # Show video
        cv2.imshow("AI Traffic Light Manager", display_frame)

        # Press Q to stop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    print(f"Processed Frames : {frame_number}")
    print("Video processing completed.")


if __name__ == "__main__":
    process_video()