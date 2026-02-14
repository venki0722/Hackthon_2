import joblib
import numpy as np

model = joblib.load("renewable_model.pkl")

sample = np.array([[60, 1012, 15]])  # Use correct feature order
prediction = model.predict(sample)

print("Prediction:", prediction)