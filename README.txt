# House Price Prediction API

This repository contains my solution for a Machine Learning Engineer assessment task. The project demonstrates the complete machine learning workflow from data preprocessing and model training to deploying a REST API for predicting house prices. The API is containerized with Docker for easy deployment.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Bonus Enhancements](#bonus-enhancements)
- [Contact](#contact)

## Overview

This project predicts house prices based on various features. It includes:
- **Data Preprocessing & Model Training:**  
  The Jupyter Notebook (`Arnav Jena - Deccan_AI.ipynb`) contains all steps for cleaning the data, handling missing values, feature engineering, and training a regression model.
- **Model Artifacts:**  
  The trained model, scaler, and feature columns are saved as `best_model.pkl`, `scaler.pkl`, and `feature_cols.pkl` respectively.
- **API Deployment:**  
  A Flask API (`app.py`) exposes a `/predict` endpoint that accepts JSON input and returns a predicted house price.
- **Containerization:**  
  A `Dockerfile` and a minimal `requirements.txt` (with Flask, pandas, numpy, scikit-learn, scipy, and joblib) are provided for building a Docker image.

## Features

- **REST API:**  
  The `/predict` endpoint accepts POST requests with JSON data and returns the predicted price.
- **Docker Containerization:**  
  The application runs inside a Docker container, ensuring consistent environments and easy deployment.
- **Logging & Error Handling:**  
  The Flask API includes basic error handling to return informative error messages.
- **End-to-End Pipeline:**  
  From data analysis in a Jupyter Notebook to model training and API deployment, the project covers the entire lifecycle.

## Project Structure





## Setup and Installation

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/housing-price-predictor.git
   cd housing-price-predictor



Create and Activate a Virtual Environment:
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate



pip install -r requirements.txt



Run the Flask Application:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




Docker Setup:

docker build -t housing-price-predictor .

docker run -d -p 5000:5000 housing-price-predictor




