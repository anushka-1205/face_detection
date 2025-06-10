# 👤 Face Detection

This is a simple Python application that performs real-time face and eye detection using OpenCV's Haar cascade classifiers. It captures video from your webcam, detects faces and eyes in the frame, and highlights them with rectangles.

---

## 🌟 Features

- Real-time face detection using `haarcascade_frontalface_default.xml`
- Eye detection within the detected face using `haarcascade_eye.xml`
- Live video feed with annotated bounding boxes

---

## 🧠 Tech Stack

| Component               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Python**             | Core programming language                                                   |
| **CV2**                | Cascade model for face detection                                            |

---

## 📈 File Description

face.py: Main script that includes the FaceDetector class and the real-time video capture loop.

---

## 🧪 Prerequisites

Install OpenCV via pip:

```bash
pip install opencv-python
```

---

## 🚀 Getting Started

1. Clone the repository or download the face.py file.
2. Open your terminal or command prompt.
3. Run the following command:
```bash
python face.py
```
4. A window will open displaying the video feed from your webcam with faces and eyes highlighted.
5. Press ESC to exit the application.


---
Author: Anushka Srivastava

