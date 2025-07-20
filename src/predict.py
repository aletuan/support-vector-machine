# src/predict.py
# Load the trained model and make a prediction

import joblib
import numpy as np

# Load model and scaler. The model and scaler are loaded from the models directory.
clf = joblib.load('models/svm_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Sample input (e.g. [5.1, 3.5, 1.4, 0.2])
sample = np.array([[5.1, 3.5, 1.4, 0.2]])

# Scale sample. The sample is scaled using the scaler.
sample_scaled = scaler.transform(sample)

# Predict
prediction = clf.predict(sample_scaled)
print("Predicted class:", prediction)
