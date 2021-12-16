import os
from flask import Flask, jsonify, request, flash, redirect, send_from_directory, abort
from flask.helpers import send_from_directory
from flask_cors import CORS
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'Vocabulary'
ALLOWED_EXT = {'csv'}

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/getVocab', methods=['GET'])
def getVocab():
    return pd.read_csv('Vocabulary/Vocabulary.csv').to_json()

# @app.route('/getVocab', methods=['GET'])
# def getVocab():
#     try:
#         return send_from_directory(UPLOAD_FOLDER, filename='Vocabulary.csv', as_attachment=True)
#     except FileNotFoundError:
#         abort(404)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/replace', methods=['POST'])
def replace():
    new_file = request.files['file']
    if new_file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if new_file and allowed_file(new_file.filename):
        filename = secure_filename('Vocabulary.csv')
        new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'Replacement upload failure'



if __name__ == '__main__':
    app.run()