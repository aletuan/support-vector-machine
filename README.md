# 🌸 SVM Iris Classifier

This project demonstrates the classification of Iris flower species using a Support Vector Machine (SVM) with a linear kernel. It serves as a small example to familiarize users with the SVM model in Machine Learning.

## 🎯 Objectives

- Apply SVM knowledge to solve a classification problem.
- Understand and practice the train/test/predict process with an SVM model.
- Calculate and visualize the decision boundary (margin).

## 📊 Data

The project uses the **Iris** dataset from `scikit-learn`, which includes 150 samples with 4 features:

- `sepal length (cm)`
- `sepal width (cm)`
- `petal length (cm)`
- `petal width (cm)`
- `species` (label: 0 = setosa, 1 = versicolor, 2 = virginica)

## 🧠 Model

- Model: `SVC(kernel='linear')` from `sklearn.svm`
- Concept: Find the optimal hyperplane to separate data.
- **Separation Formula**:  
  `yᵢ (w ⋅ xᵢ + b) ≥ 1` for all i  
  ⇒ The distance between the two margins is **2 / ||w||**

## 📁 Project Structure

```
svm_iris_classifier/
├── data/                   # (Optional) Location to store iris.csv if needed
├── models/                 # Stores trained models (e.g., svm_model.pkl)
├── notebooks/              # Jupyter notebooks for data exploration (EDA)
├── src/                    # Main source code
│   ├── train.py            # Trains and evaluates the model
│   ├── predict.py          # Makes predictions on new samples
│   └── utils.py            # Helper functions (if any)
├── requirements.txt        # Required libraries
└── README.md
```

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python src/train.py
```

### 3. Predict New Samples

```bash
python src/predict.py
```

