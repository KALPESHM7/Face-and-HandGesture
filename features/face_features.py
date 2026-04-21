# features/face_features.py

def is_mouth_open(face_landmarks, threshold=0.02):
    if face_landmarks is None:
        return False

    landmarks = face_landmarks.landmark

    # Upper lip and lower lip
    upper_lip = landmarks[13]
    lower_lip = landmarks[14]

    # Distance between lips
    distance = abs(upper_lip.y - lower_lip.y)

    if distance > threshold:
        return True
    return False