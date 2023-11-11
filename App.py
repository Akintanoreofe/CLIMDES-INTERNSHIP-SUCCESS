from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Loading the trained logistic regression model
model = joblib.load("trained_logistic_model.pkl")

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Getting data from the request's query parameters
        data = request.args.to_dict()
        if not data:
            return jsonify({"error": "No data provided"})

        # Converting input data to a DataFrame
        input_data = pd.DataFrame(data, index=[0])

        # Making predictions using the trained model
        predictions = model.predict(input_data)

        # Returning the predictions as JSON
        response = {"predictions": predictions.tolist()}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(port=4996)