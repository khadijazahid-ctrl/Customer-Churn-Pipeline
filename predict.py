import pandas as pd
import joblib

model = joblib.load("models/churn_pipeline.pkl")

sample = pd.read_csv("TelcoCustomerChurn.csv")

prediction = model.predict(sample)

print(prediction)