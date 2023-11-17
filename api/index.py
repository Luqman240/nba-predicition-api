from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import os



app = Flask(__name__)
CORS(app)
# Load your pre-trained model
#model = pickle.load(open('nba-result-ml.pkl', 'rb'))
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the file
file_path = os.path.join(current_directory, 'nba-result-ml.pkl')

with open(file_path, 'rb') as f:
    model = pickle.load(f)
    
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
@app.route('/')
def hello_world():
    return 'This is the NBA Result Prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()
         # Make predictions using your model
        result = model.predict([np.array(data["input"])])
        output = result[0]
        # Return the predictions as JSON
        return jsonify({'result': output})
       
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
