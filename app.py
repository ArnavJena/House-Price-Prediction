# app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the saved model, scaler, and feature columns
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('feature_cols.pkl', 'rb') as f:
    feature_cols = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve JSON data from the POST request
        data = request.get_json(force=True)
        
        # Convert input data (dictionary) to DataFrame
        input_df = pd.DataFrame([data])
        
        # Check if all required features are provided
        missing_features = [feat for feat in feature_cols if feat not in input_df.columns]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400
        
        # Reorder the DataFrame columns to match training features
        input_df = input_df[feature_cols]
        
        # Scale the input data
        input_scaled = scaler.transform(input_df)
        
        # Predict using the loaded model
        prediction = model.predict(input_scaled)
        
        # Return the prediction as JSON
        return jsonify({"predicted_price": float(prediction[0])})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)