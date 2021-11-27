from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

from software_requirement_classifier import DataProcessor
from main import main

software_requirement_classifier_obj = DataProcessor()

app = Flask(__name__)
CORS(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UML_GENERATOR_UPLOAD_FOLDER = os.path.join(APP_ROOT,'uploads')
OUTPUTS_FOLDER = os.path.join(APP_ROOT,'outputs')

app.config['UML_GENERATOR_UPLOAD_FOLDER'] = UML_GENERATOR_UPLOAD_FOLDER

######################################## UML GENERATOR ROUTES ########################################

@app.route('/process-transcript', methods=['POST'])
def process_requirements_docx():
    if request.method == 'POST':
        file = request.files['transcriptFile']
        file.save(os.path.join(app.config['UML_GENERATOR_UPLOAD_FOLDER'], secure_filename(file.filename)))
        result = software_requirement_classifier_obj.run(file.filename)
        return jsonify(results=result)

@app.route('/process-uml-diagrams-inputs', methods=['POST'])
def process_uml_diagrams():
    if request.method == 'POST':
        file = request.files['scenarioFile']
        file.save(os.path.join(app.config['UML_GENERATOR_UPLOAD_FOLDER'], secure_filename(file.filename)))
        generated_class_diagram_path,generated_usecase_diagram_path,generated_activity_diagram_path = main(file.filename)
        return jsonify(generated_class_diagram_path=generated_class_diagram_path,generated_usecase_diagram_path=generated_usecase_diagram_path,generated_activity_diagram_path=generated_activity_diagram_path)

@app.route('/view-diagram/<path:path>')
def send_js(path):
    return send_from_directory(OUTPUTS_FOLDER, path)

######################################################################################################
if __name__ == '__main__':
    app.run(port=5000, debug=True)
