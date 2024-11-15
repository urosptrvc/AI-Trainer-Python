# Fitness Tracker with Pose Detection

A real-time fitness tracker that uses pose detection to count repetitions of arm exercises for both left and right arms. This project utilizes OpenCV and a custom `PoseModule` to track body movements and calculate the angles of the arms.

## Features
- **Pose Detection**: Tracks the user's body position using a webcam.
- **Repetition Counting**: Counts the number of completed repetitions for both left and right arms.
- **Progress Bar**: Displays a progress bar and percentage for each arm.
- **Real-Time Feedback**: Shows live feedback with a clear and user-friendly interface.
- **FPS Counter**: Displays the real-time frames per second (FPS) to monitor performance.

## Prerequisites
- Python 3.7 or higher
- A webcam
- Required Python libraries:
  - `numpy`
  - `opencv-python`
  - Custom `PoseModule` (not included in this repository—ensure you have this file or package)
