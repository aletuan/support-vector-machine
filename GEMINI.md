# Project Context for Gemini CLI Agent

This file provides essential context for the Gemini CLI agent to effectively understand and interact with this machine learning project.

## 1. Project Overview

- **Project Type**: Machine Learning (Support Vector Machine Classification)
- **Purpose**: Classify Iris flower species using a linear SVM.
- **Primary Language**: Python

## 2. Key Directories and Files

- `data/`: Intended for storing datasets (e.g., `iris.csv`). Currently, the `train.py` script loads the Iris dataset directly from `sklearn.datasets`.
- `models/`: Stores trained machine learning models (`.pkl` files) and the `StandardScaler` used for feature scaling.
  - `models/svm_model.pkl`: Trained SVM classifier.
  - `models/scaler.pkl`: Fitted `StandardScaler` object.
- `notebooks/`: Contains Jupyter notebooks for data exploration, experimentation, or visualization.
- `src/`: Contains the core Python scripts for the ML pipeline.
  - `src/train.py`: Script for training the SVM model, evaluating its performance, and saving the model and scaler.
  - `src/predict.py`: Script for loading the trained model and scaler, and making predictions on new data.
- `requirements.txt`: Lists all Python dependencies required for the project (e.g., `scikit-learn`, `numpy`, `joblib`).
- `README.md`: Project overview, setup instructions, and how to run the scripts.
- `docs/SVM_Basics.md`: Explains basic concepts of Linear Support Vector Machines for beginners.

## 3. Development Workflow

### Installation
- Dependencies are managed via `requirements.txt`.
- To install: `pip install -r requirements.txt`

### Training
- To train the model: `python src/train.py`
- This script will save the trained model and scaler to the `models/` directory.

### Prediction
- To make predictions: `python src/predict.py`
- This script loads the saved model and scaler from `models/`.

## 4. Technical Details

- **Model**: Support Vector Classifier (SVC) with a linear kernel (`sklearn.svm.SVC(kernel='linear')`).
- **Data Preprocessing**: `StandardScaler` is used for feature scaling. It's crucial to use the *same* fitted scaler for both training and prediction.
- **Model Persistence**: `joblib` is used to save and load the trained model and scaler.

## 5. Testing and Linting

- **Testing Framework**: No explicit unit testing framework (e.g., `pytest`) is currently set up for this project.
- **Linting/Formatting**: No explicit linting or code formatting tools (e.g., `flake8`, `black`) are currently configured.

## 6. User Preferences

- **Unit Tests**: The user has explicitly stated that I should *not* run unit tests automatically after making changes.
