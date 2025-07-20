# 🌸 SVM Iris Classifier

Phân loại loài hoa Iris bằng Support Vector Machine (SVM) với kernel tuyến tính. Dự án này là một ví dụ nhỏ giúp làm quen với mô hình SVM trong Machine Learning.

## 🎯 Mục tiêu

- Áp dụng kiến thức về SVM để giải bài toán phân loại.
- Hiểu và thực hành quá trình train/test/predict với mô hình SVM.
- Tính toán và trực quan hóa đường biên phân cách (margin).

---

## 📊 Dữ liệu

Sử dụng bộ dữ liệu **Iris** từ `scikit-learn`, bao gồm 150 mẫu với 4 thuộc tính:

- `sepal length (cm)`
- `sepal width (cm)`
- `petal length (cm)`
- `petal width (cm)`
- `species` (label: 0 = setosa, 1 = versicolor, 2 = virginica)

---

## 🧠 Mô hình

- Mô hình: `SVC(kernel='linear')` từ `sklearn.svm`
- Ý tưởng: Tìm siêu phẳng phân chia dữ liệu tối ưu.
- **Công thức phân chia**:  
  `yᵢ (w ⋅ xᵢ + b) ≥ 1` với ∀i  
  ⇒ Khoảng cách giữa 2 biên là **2 / ||w||**

---

## 📁 Cấu trúc thư mục

svm_iris_classifier/
├── data/                   # (tùy chọn) nơi lưu file iris.csv nếu cần
├── models/                 # Lưu model đã train (svm_model.pkl)
├── notebooks/              # Notebook khám phá dữ liệu (EDA)
├── src/                    # Mã nguồn chính
│   ├── train.py            # Huấn luyện và đánh giá mô hình
│   ├── predict.py          # Dự đoán với mẫu mới
│   └── utils.py            # Hàm phụ trợ (nếu cần)
├── requirements.txt        # Thư viện cần thiết
└── README.md

---
## 🚀 Cách chạy

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 2. Train mô hình

```bash
python src/train.py
```

### 3. Dự đoán mẫu mới

```bash
python src/predict.py
```

