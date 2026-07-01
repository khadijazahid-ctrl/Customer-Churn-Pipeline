# Customer Churn Prediction using Scikit-learn Pipeline

## Objective

Build a reusable and production-ready machine learning pipeline for predicting customer churn using the Scikit-learn Pipeline API.

## Dataset

Telco Customer Churn Dataset

## Methodology / Approach

- Load and clean the dataset
- Handle missing values
- Encode categorical variables
- Scale numerical features
- Build preprocessing pipelines using Pipeline and ColumnTransformer
- Train Logistic Regression and Random Forest models
- Tune hyperparameters using GridSearchCV
- Evaluate models using Accuracy, Classification Report, and Confusion Matrix
- Export the best-performing model using Joblib

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

## Repository Structure

```
GridSearch.csv
TelcoCustomerChurn.csv
models/
Customer_Churn_Pipeline.ipynb
train.py
predict.py
README.md
requirements.txt
```

## Key Results / Observations

- Built a complete end-to-end machine learning pipeline.
- Automated preprocessing using Scikit-learn Pipeline API.
- Compared Logistic Regression and Random Forest models.
- Used GridSearchCV to identify optimal hyperparameters.
- Saved the best model for future predictions.
- Created a reusable and production-ready workflow.

## Results

Two models were trained:

- Logistic Regression
- Random Forest

The best-performing pipeline was selected using GridSearchCV and saved as `churn_pipeline.pkl`.

## How to Run

Train the model:

```bash
python train.py
```

Predict using the saved model:

```bash
python predict.py
```

## Author
Khadija Zahid
