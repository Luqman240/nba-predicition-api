from flask import Flask, jsonify, request, send_from_directory
import pickle
import numpy as np
import os

app = Flask(__name__)


    
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
@app.route('/')
def hello_world():
    return 'This is the NBA Result Prediction API!'


if __name__ == '__main__':
    app.run(debug=True)
