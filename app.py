from flask import Flask, render_template, Response
import cv2
from modules.hand_tracker import HandTracker
from modules.gesture_recognizer import GestureRecognizer
from utils.helpers import draw_text, draw_circle

app = Flask(__name__)

hand_tracker = HandTracker()
gesture_recognizer = GestureRecognizer()

cap = cv2.VideoCapture(0)

def gen_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  
        frame, results = hand_tracker.find_hands(frame)

        landmarks = hand_tracker.get_landmarks(results, frame)
        
        gesture = gesture_recognizer.detect_gesture(landmarks)
        if gesture:
            draw_text(frame, gesture, (50, 100)) 
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
