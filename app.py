import os
import json
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
# app = Flask(__name__)
# api = Api(app)
# CORS(app)
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def home():
    try:
        return {'data': 'L.U.N.A.L.A API is Running'}
    except:
        return {'data': 'An Error Occurred during fetching Api'}

@app.route('/getAuth', methods=['GET'])
def getAuth():
    try:
        dict = {}
        with open('Credentials/Credentials.txt') as fh:
            for line in fh:
                creds = line.strip().split(',', 1)
                dict[creds[0]] = creds[1]
            return json.dumps(dict)
    except: 
        return {'data': 'An error ocurred retrieving credentials'}

@app.route('/getCSV', methods=['GET'])
def getCSV():
    try:
        return send_from_directory('Vocabulary', filename='Vocabulary.csv', as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/getVocab', methods=['GET'])
def getVocab():
    try:
        return pd.read_csv('Vocabulary/Vocabulary.csv').to_json()
    except:
        return {'data': 'Failed to retrieve vocabulary'}

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
    return {'data': 'Replacement upload failure'}

@app.route('/saveCSV', methods=['POST'])
def saveSCV():
    try:
        new_file_obj = request.get_json()
        df = pd.read_json(json.dumps(new_file_obj))
        df.to_csv('Vocabulary/Vocabulary.csv', encoding='utf-8', index=False)
        print("Accepted CSV:\n", df)
        return 'Success'
    except:
        return {'data': 'CSV failed to save'}


if __name__ == '__main__':
    app.run()