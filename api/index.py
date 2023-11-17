from flask import Flask, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your pre-trained model
model = pickle.load(open('./nba-result-ml.pkl'))

@app.route('/')
def hello_world():
    return 'This is the NBA Result Prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Make predictions using your model
        result = model.predict([[np.array(data['input'])]])
        output = result[0]
        # Return the predictions as JSON
        return jsonify({'result': output})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
