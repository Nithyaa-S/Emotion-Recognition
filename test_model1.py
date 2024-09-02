import mimetypes
import os
import pickle
import cv2
from utils import get_face_landmarks
from flask import Flask, jsonify, request, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

emotions = ['SURPRISED', 'SAD', 'HAPPY']

with open('../model', 'rb') as f:
    model = pickle.load(f)

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def check():
    return 'Hello'

def save_file(file):
    if file.filename == '':
        return None, "No selected file"
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return file_path, None

def predict(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    frame = cv2.imread(file_path)
    
    if frame is None:
        return None, "Unable to read image file"
    
    face_landmarks = get_face_landmarks(frame, static_image_mode=False)  # draw=True

    if face_landmarks is not None:
        output = model.predict([face_landmarks])
        emotion = emotions[int(output[0])]
        cv2.putText(frame, emotion, (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)
        
        # Save the processed image
        cv2.imwrite(file_path, frame)

        mime_type, _ = mimetypes.guess_type(file_path)
        return file_path, emotion
    
    return None, "No face landmarks detected"

@app.route('/predict', methods=['POST'])
def predict_call():
    if 'image' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['image']
    file_path, save_error = save_file(file)
    
    if save_error:
        return jsonify({"error": save_error}), 400
    
    processed_file_path, emotion = predict(file.filename)
    
    if not processed_file_path:
        return jsonify({"error": "Image processing failed"}), 500
    
    #image_url = url_for('check', filename=processed_file_path, _external=True)
    image_url = ('http://localhost:5501/uploads/captured_image.png')
    print("Processed file path:", processed_file_path)  # Debugging: print the file path
    print("Image URL:", image_url)  # Debugging: print the image URL
    print("image name:", file.filename )
    print("image emotion", emotion)

    return jsonify({
        
        'imageURL': image_url,
        'text': emotion
    })

if __name__ == '__main__':
    app.run(debug=True)
