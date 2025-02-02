import cv2
from modules.hand_tracker import HandTracker
from modules.gesture_recognizer import GestureRecognizer
from utils.helpers import draw_text, draw_circle

hand_tracker = HandTracker()
gesture_recognizer = GestureRecognizer()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  
    frame, results = hand_tracker.find_hands(frame)

    landmarks = hand_tracker.get_landmarks(results, frame)
    
    gesture = gesture_recognizer.detect_gesture(landmarks)

    draw_text(frame, "Hand Detected", (50, 50))
    draw_circle(frame, (100, 100))  

    if gesture:
        draw_text(frame, gesture, (50, 100))  

    cv2.imshow("Hand Tracking AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
