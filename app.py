import streamlit as st
from main_video import process_video

st.set_page_config(page_title="Face Recognition Video Processor", layout="wide")

def home():
    st.title("Face Recognition Basesd Video Segmentation")
    st.markdown("""

## **Project Overview**  
This project utilizes **YOLO** (You Only Look Once), a state-of-the-art object detection model, along with **OpenCV**, a popular computer vision library, to efficiently detect and recognize faces in videos. The main objective is to clip specific segments of the input video containing the desired face, allowing users to upload both a video and a reference image to identify the person in real-time. The system processes the video and generates a clipped version, focusing only on the moments where the target face appears.

---""")
    st.image("Project_1_Use_Case.png")
    st.markdown("""---

## **System Architecture**  

### **1. YOLO for Face Detection**  
The **YOLO model** is a real-time object detection algorithm that breaks down the input image into a grid and predicts bounding boxes along with class probabilities. For this project, **YOLO-v10** models are fine-tuned specifically to detect faces with high accuracy. Unlike traditional sliding window techniques, YOLO performs detection in a single pass, making it both **fast and efficient**.  
- **Advantages of YOLO:**
  - High-speed face detection with minimal latency.
  - Ability to detect multiple faces in a single frame.
  - Works comparatively well with videos of varying resolutions.

---

### **2. OpenCV for Video Processing and Face Recognition**  
OpenCV is used to:
- **Process each video frame** extracted by the video capture module.
- **Compare the detected faces** using facial embeddings generated from the uploaded reference image.
- **Draw bounding boxes and labels** around recognized faces, improving the user’s visibility and feedback.

The face recognition step leverages **OpenCV’s facial comparison functionality** along with **cosine similarity** or **Euclidean distance** between facial embeddings. This ensures that the correct individual is identified across multiple frames. The OpenCV library also enables efficient handling of videos by:
- **Extracting frames** at a defined FPS.
- **Encoding the clipped output video** with high-quality compression.

---""")
    st.image("Project_1_Final.png")
    st.markdown("""## **Process Flow**  

1. **Input:**
   - The user uploads a **video file** and a **face image**.
2. **Face Detection:**
   - YOLO detects faces in each frame of the input video and returns bounding boxes.
3. **Face Recognition:**
   - OpenCV compares the detected faces with the uploaded image to determine matches.
4. **Video Clipping:**
   - If a match is found, the corresponding frame is **written to the output video**.
5. **Output:**
   - The user downloads the **clipped video**, containing only the segments where the target face appears.

---

## **Key Technologies Used**  

- **YOLO:** For fast and accurate face detection.
- **OpenCV:** For video handling, frame extraction, and facial comparison.
- **Streamlit:** Frontend and Backend web framework to process video and manage user inputs.

---

## **Advantages of the YOLO + OpenCV Approach**  

1. **High Performance:**  
   YOLO ensures high-speed detection, making the solution ideal for **real-time applications**.

2. **Scalable and Robust:**  
   The system can handle **multiple face detections** per frame and large video files efficiently.

3. **Easy Integration:**  
   The combined use of OpenCV and Streamlit ensures a smooth **backend and frontend interaction**, providing an effortless user experience.

4. **Optimized for Recognition:**  
   The integration of **OpenCV for facial matching** ensures that only the desired segments are included in the final output, minimizing processing overhead.

---

## **Future Scope**  
- **Model Fine-tuning:** Fine-tune the YOLO model to handle occluded or low-quality faces.
- **GPU Acceleration:** Leverage GPU-based computation for faster processing on larger videos.
- **Advanced Features:** Implement features like **blurred face masking** or **multi-face detection and clipping** in future versions.

---

This **YOLO + OpenCV architecture** ensures that the system is both **accurate and performant**, making it suitable for applications such as **surveillance video filtering**, **highlight reel generation**, and **face-based video analytics**. 

---    """)

def video_processor():
    st.title("Upload Image and Video")

    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    uploaded_video = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

    if uploaded_image and uploaded_video:
        if st.button("Process Video"):
            image_path = f"person_image.jpg"
            video_path = f"video_footage.mp4"
            output_path = "segmented_video.mp4"

            with open(image_path, "wb") as f:
                f.write(uploaded_image.read())
            with open(video_path, "wb") as f:
                f.write(uploaded_video.read())

            with st.spinner("Processing..."):
                output = process_video(image_path, video_path, output_path)
                st.success("Processing complete!")

                # Display video
                st.video(output)

                # Provide download link
                with open(output, "rb") as f:
                    st.download_button(
                        label="Download Processed Video",
                        data=f,
                        file_name="processed_video.mp4",
                        mime="video/mp4"
                    )

# Streamlit multipage layout
page = st.sidebar.selectbox("Choose a page", ["Home", "Process Video"])

if page == "Home":
    home()
else:
    video_processor()
