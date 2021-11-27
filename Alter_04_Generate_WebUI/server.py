from flask import Flask, render_template, request
from flask_cors import CORS 
from template_matching import generatecode
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'img/'

@app.route('/genereatecode', methods=['GET', 'POST'])
def generate_code():
    if request.method == 'POST':
        try:
            file = request.files['file']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            htmlcode = generatecode(file.filename)
            return htmlcode
        except:
            return "Please Upload valid Wireframe"

if __name__ == '__main__':
    app.run(port=5002, debug=True)




