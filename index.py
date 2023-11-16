from flask import Flask;
from flask import Flask, jsonify, request
import sklearn  # Replace with the library you used to train your model
import pickle

app = Flask(__name__)

# Load your pre-trained model
model = pickle.load('./nba-result-ml.sav')

@app.route('/')
def hello_world():
    return 'This is the NBA Result Prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Make predictions using your model
        result = model.predict(data['input'])

        # Return the predictions as JSON
        return jsonify({'result': result.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
