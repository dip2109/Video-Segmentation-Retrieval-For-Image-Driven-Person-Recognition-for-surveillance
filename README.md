# Video-Segmentation-Retrieval-For-Image-Driven-Person-Recognition-for-surveillance

# Project Overview
This project implements image-driven video segmentation for surveillance, leveraging YOLOv10 and OpenCV for efficient face detection, recognition, and video processing. By analyzing video footage based on a reference image, the system identifies specific individuals and segments relevant clips for streamlined surveillance and analysis. Designed for real-time applications, it is an effective tool for law enforcement and public safety.

# Key Features
**1. Real-Time Detection and Segmentation:** Fast and accurate face detection powered by YOLOv10.
**2. Image-Driven Person Recognition:** Matches faces in video frames with a provided image for targeted surveillance.
**3. Automated Video Clipping:** Outputs video segments focusing on frames with the identified person.
**4. User-Friendly Interface:** Built with Streamlit for intuitive interaction.

# System Architecture
The system integrates the following technologies:

**YOLOv10:** For efficient face detection.
**OpenCV:** For frame extraction, face recognition, and video processing.
**Streamlit:** For a simple and interactive user interface.

# Process Flow
**Input:**
1. Upload a video file (e.g., .mp4, .avi)
2. Upload a reference image (e.g., .jpg, .png)

# Processing:
YOLOv10 detects faces in video frames.
OpenCV matches detected faces with the reference image.
Frames with matches are compiled into a new video.

# Output:
A downloadable video containing relevant segments is generated.

![Project_1_Final](https://github.com/user-attachments/assets/b63a6504-38ee-42f4-8ea1-1c9461cdf0a9)

# Demo
# Input
**Upload:**
1. A video file (e.g., .mp4, .avi).
2. A person image (e.g., .jpg, .png).

**Eg.**
[![Input Image]](https://github.com/dip2109/Video-Segmentation-Retrieval-For-Image-Driven-Person-Recognition-for-surveillance/blob/main/Tom_Cruise.jpg)
[![Input Video]](https://github.com/dip2109/Video-Segmentation-Retrieval-For-Image-Driven-Person-Recognition-for-surveillance/blob/main/video_footage.mp4)

**Output**
Download the processed video with highlighted segments.
[![Output Video]](https://github.com/dip2109/Video-Segmentation-Retrieval-For-Image-Driven-Person-Recognition-for-surveillance/blob/main/segmented_video.mp4)


# Technologies Used
1. YOLOv10: For high-performance face detection.
2. OpenCV: For frame processing and face recognition.
3. Streamlit: For the interactive user interface.

# Future Scope
1. Enhanced Detection: Improve the system's ability to handle occluded or low-quality faces.
2. Real-Time Processing: Leverage advanced GPU acceleration for faster video analysis.
3. Advanced Features: Add multi-face detection and tracking capabilities.

