import cv2

class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_eye.xml'
        )

    def detect_and_annotate(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return frame

def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        annotated = detector.detect_and_annotate(frame)
        cv2.imshow('Face & Eye Detection', annotated)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

# pip install opencv-python
# to run: python face.py
# click ESC to escape the box
