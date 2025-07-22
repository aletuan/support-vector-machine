# src/train.py
# Train a linear SVM classifier on the Iris dataset

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Loading the well-known Iris dataset, which contains features of different iris flower species.
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Standardize features. This step is crucial for SVMs as it ensures that all features contribute equally to the model's training, preventing features with larger numerical ranges from dominating
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split. 80% of the data is used to train the model, and the remaining 20% is held out to evaluate its performance
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train SVM with linear kernel. This is a simple SVM model that uses a linear kernel to separate the data into different classes.
clf = SVC(kernel="linear")
clf.fit(X_train, y_train)

# Evaluate. The model's performance is evaluated using the test set.
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model and scaler. The model and scaler are saved to the models directory.
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/svm_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
