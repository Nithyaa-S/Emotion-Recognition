from flask import *
import cv2
import pickle
from utils import get_face_landmarks

app = Flask(__name__)

# Load the trained model
with open('./model.pkl', 'rb') as f:
    model = pickle.load(f)

emotions = ['SURPRISED', 'SAD', 'HAPPY']

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_landmarks = get_face_landmarks(frame, static_image_mode=False)

        if face_landmarks and len(face_landmarks) == 1404:
            output = model.predict([face_landmarks])
            cv2.putText(frame, emotions[int(output[0])], (10, frame.shape[0] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

