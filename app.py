from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
import tensorflow as tf
import base64
from net.face import detect_faces , detect_objects

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

@app.route('/detect_object', methods=['POST'])
def detect_object():
    print('Received request:')
    print(request.files)
    print(request.form)

    if 'image' not in request.files:
        print('No image')
        return jsonify({'error': 'No image provided'}), 400

    print('Got image')
    image = request.files['image']
    filename = secure_filename(image.filename)
    uploaded_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    image.save(uploaded_path)
    image_file = cv2.imread(uploaded_path)
    # Perform cat/dog classification
    # result_image_base64 = detect_objects(image_file)

    # Perform face detection and update the result image
    # result_image_base64 = detect_faces(image_file)
    result_image_base64= detect_objects(image_file)
    _, buffer = cv2.imencode('.jpg', result_image_base64)
    face_base64 = base64.b64encode(buffer).decode('utf-8')


    print('Object detected')
    return jsonify({'result_image_base64': face_base64})


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=8080)
