from flask import Flask, jsonify, request, send_from_directory
import pickle
import numpy as np

app = Flask(__name__)

# Load your pre-trained model
#model = pickle.load(open('nba-result-ml.pkl', 'rb'))
model = piclke.load(send_from_directory(os.path.join(app.root_path, 'static'), 'nba-result-ml.pkl'))
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
        result = model.predict([[np.array(data['input'])]])
        output = result[0]
        # Return the predictions as JSON
        return jsonify({'result': output})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)