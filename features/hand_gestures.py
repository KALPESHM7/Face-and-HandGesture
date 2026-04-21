# features/hand_gestures.py

def count_fingers(hand_landmarks):
    if hand_landmarks is None:
        return 0

    landmarks = hand_landmarks.landmark

    fingers = []

    # Thumb (simple logic)
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]

    for tip, pip in zip(tip_ids, pip_ids):
        if landmarks[tip].y < landmarks[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)


# 🔥 NEW: Gesture recognition
def get_gesture(hand_landmarks):
    if hand_landmarks is None:
        return "No Hand"

    landmarks = hand_landmarks.landmark

    fingers = []

    # Thumb
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]

    for tip, pip in zip(tip_ids, pip_ids):
        if landmarks[tip].y < landmarks[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    total = sum(fingers)

    # 🔥 Gesture rules
    if total == 0:
        return "Fist ✊"
    elif total == 5:
        return "Open Hand 🖐"
    elif fingers[1] == 1 and fingers[2] == 1 and total == 2:
        return "Peace ✌️"
    elif fingers[0] == 1 and total == 1:
        return "Thumbs Up 👍"
    elif fingers[1] == 1 and total == 1:
        return "Pointing ☝️"
    else:
        return f"{total} Fingers"