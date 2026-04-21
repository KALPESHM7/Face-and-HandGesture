# main.py

import cv2
from config import *
from modules.detector import HolisticDetector
from modules.drawer import draw_landmarks
from modules.utils import FPS

# Features
from features.hand_gestures import count_fingers, get_gesture
from features.face_features import is_mouth_open

# Initialize
detector = HolisticDetector()
fps_counter = FPS()

cap = cv2.VideoCapture(CAMERA_INDEX)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize
    frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

    # Convert BGR → RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect landmarks
    results = detector.process(rgb)

    # Finger counting
    right_count = count_fingers(results.right_hand_landmarks)
    left_count = count_fingers(results.left_hand_landmarks)
    total = right_count + left_count

    # 🔥 Gesture recognition
    right_gesture = get_gesture(results.right_hand_landmarks)
    left_gesture = get_gesture(results.left_hand_landmarks)

    # Face feature
    mouth_open = is_mouth_open(results.face_landmarks)

    # Draw landmarks
    frame = draw_landmarks(frame, results)

    # FPS
    cv2.putText(frame, f"FPS: {fps_counter.calculate()}",
                (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Finger counts
    cv2.putText(frame, f"Right: {right_count}",
                (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(frame, f"Left: {left_count}",
                (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(frame, f"Total: {total}",
                (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # 🔥 Gesture display
    cv2.putText(frame, f"Right Gesture: {right_gesture}",
                (300, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.putText(frame, f"Left Gesture: {left_gesture}",
                (300, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Face info
    cv2.putText(frame, f"Mouth Open: {mouth_open}",
                (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Show
    cv2.imshow("Smart Gesture Recognition System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()