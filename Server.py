from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from keras.preprocessing import image
import tensorflow as tf
import cv2
import numpy as np
import os
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\DuminduS\AppData\Local\Programs\Tesseract-OCR\tesseract'
from PIL import Image

model = tf.keras.models.load_model('../Models/Diagram_Identification.h5')
app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'Image_Upload/'


def predict_result(img_name):
    predict_class = ["Usecase Diagram", "Activity Diagram", "Class Diagram"]
    img = image.load_img(app.config['UPLOAD_FOLDER'] + img_name, target_size=(150, 150))
    img = image.img_to_array(img) / 255.0
    img = img.reshape(1, 150, 150, 3)
    y_pred = model.predict(img)
    y_class = [np.argmax(element) for element in y_pred]
    imge = Image.open(app.config['UPLOAD_FOLDER'] + img_name)
    results = tess.image_to_string(imge)

    response = {
        "class": predict_class[y_class[0]],
        "lables": results
    }
    return response

@app.route('/uploader', methods=['GET', 'POST'])
def predict_img():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        result = predict_result(file.filename)
        return result

if __name__ == '__main__':
    app.run(port=5001, debug=True)
