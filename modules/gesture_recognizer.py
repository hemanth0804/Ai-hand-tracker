class GestureRecognizer:
    @staticmethod
    def detect_gesture(landmarks):
        if not landmarks or len(landmarks) < 21:
            return None

        # Key landmark indices
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        wrist = landmarks[0]

        # Gesture 1: 👍 **Thumbs Up**
        if thumb_tip[1] < index_tip[1] and thumb_tip[1] < middle_tip[1]:  
            return "Thumbs Up"


        fingers_up = sum(1 for tip in [thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip] if tip[1] < wrist[1])
        if fingers_up == 5:
            return "Open Palm"


        return "Unknown Gesture"
