# CLIMDES-INTERNSHIP-SUCCESS
# Internship Success Prediction

This project aims to predict the success of an intern using machine learning. A logistic regression model is trained on simulated data to predict whether an applicant will succeed in completing their internship.

## Data Generation and Preprocessing

Simulated data for the model includes various factors such as academic performance, relevant skills, experience, weekly hours available, laptop availability, and constant internet access. The success criteria for internship applicants are defined based on a combination of these factors.

### Data Simulation and Preprocessing

- Simulate data for 3000 applicants.
- Simulated factors include academic performance, relevant skills, experience, weekly hours available, laptop availability, and constant internet access.
- Define success criteria based on a combination of these factors.

### Data Cleaning

- Load the simulated dataset and perform basic data cleaning.
- Handle missing values, drop columns with excessive missing values, and convert data types as part of the cleaning process.

## Model Training and Evaluation

Logistic regression is used for training the model, employing hyperparameter tuning with grid search. The model is evaluated on a test set, and performance metrics such as accuracy, precision, recall, and a confusion matrix are computed.

### Logistic Regression Model Training

- Train the logistic regression model on the cleaned dataset.
- Perform hyperparameter tuning using grid search.

### Model Evaluation

- Evaluate the trained model on a test set.
- Compute performance metrics (accuracy, precision, recall).
- Create and visualize a confusion matrix as a heatmap.

## Model Interpretation with SHAP Values

To interpret the model's decisions, SHAP (SHapley Additive exPlanations) values are calculated. SHAP values provide insight into the impact of each feature on the model's output.

### SHAP Values Calculation

- Compute SHAP values using the KernelExplainer from the SHAP library.
- Explain the model's decisions by visualizing the summary plot of SHAP values.

## API for Model Predictions

An API is provided for making predictions using the trained logistic regression model. Send input data as query parameters, and the API will return predictions in JSON format.

### API Usage

- Host the API using Flask.
- Send a GET request to the `/predict` endpoint with input data as query parameters(http://localhost:4996/predict?Academic%20Performance%20(GPA)=2.5&Relevant%20Skills%20(0-10)=7&Experience%20(Months)=24&Weekly%20Hours%20Available=30&Laptop%20Availability=1&Constant%20Internet%20Access=1).
- The API returns predictions in JSON format.

## Dependencies

- Flask
- Joblib
- Matplotlib
- Numpy
- Pandas
- Scikit-learn
- Seaborn
- Shap

## How to Run

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the Flask app using `python app.py`.

