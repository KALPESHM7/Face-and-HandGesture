# modules/detector.py

import mediapipe as mp
from config import MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE

class HolisticDetector:
    def __init__(self):
        self.mp_holistic = mp.solutions.holistic
        
        self.model = self.mp_holistic.Holistic(
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )

    def process(self, image):
        image.flags.writeable = False
        results = self.model.process(image)
        image.flags.writeable = True
        return results