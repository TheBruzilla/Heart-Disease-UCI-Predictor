# Heart-Disease-UCI-Predictor-
This project focuses on developing a Disease Prediction Toolkit using machine learning techniques to analyze real-world healthcare datasets. By applying models such as Logistic Regression, Decision Trees, and Random Forests, we aim to build accurate predictors of heart disease and similar conditions.

# 🩺 Disease Prediction Toolkit: Building and Evaluating ML Models

This project was developed as part of the **Save Lives with AI Bootcamp**.  
It demonstrates how to preprocess healthcare datasets, build machine learning models, and evaluate their performance for disease prediction.

---

## 📌 Project Overview
Healthcare datasets often contain categorical and numeric features with missing values.  
This project walks through the end-to-end ML pipeline:
- Data preprocessing (handling missing values, encoding categorical features, scaling)
- Model training (Logistic Regression, Decision Tree, Random Forest)
- Model evaluation (Accuracy, Precision, Recall, F1-score, ROC-AUC)
- Visualization (Confusion Matrix, ROC Curve, Feature Importance)
- Saving models and creating a user-friendly prediction toolkit

---

## 🎯 Learning Outcomes
- Understand fundamentals of machine learning for healthcare
- Apply preprocessing techniques for real-world medical datasets
- Train and evaluate ML classifiers with scikit-learn
- Interpret results with performance metrics and plots
- Package models for real-world use (inference-ready)

---

## 📂 Dataset
We use the [UCI Heart Disease dataset](https://www.kaggle.com/redwankarimsony/heart-disease-data).  
Other healthcare datasets (like Diabetes) can also be integrated.

**Features include:**  
- Demographics (age, sex)  
- Health indicators (blood pressure, cholesterol, blood sugar)  
- ECG results, exercise-induced angina  
- Thalassemia, slope, and other categorical tests  

**Target column (`num`)**:  
- `0` = No disease  
- `1+` = Presence of disease (binarized to 1)

---

## 🚀 Project Workflow

### 1. Data Preprocessing
- Handle missing values (mean for numerics, "Unknown" for categoricals)
- Encode categorical features with One-Hot Encoding
- Scale numeric features using StandardScaler

### 2. Model Training
- Split data into training and test sets (80/20)
- Train models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Save best model (`.pkl`) with joblib

### 3. Model Evaluation
- Accuracy, Precision, Recall, F1-score, ROC-AUC
- Confusion Matrix heatmap
- Feature Importance (Random Forest)

### 4. Prediction Toolkit
- Sample template: `heart_user_template.csv`
- Users can upload their data for predictions
- Outputs `Heart_Disease_Prediction` (0 = No disease, 1 = Disease)

---

## 📊 Results & Visuals
- Logistic Regression achieved strong baseline accuracy
- Random Forest improved performance and provided feature importance
- Example outputs include Confusion Matrix and Feature Importance bar plots

---

## 📝 Author
 **Vishal N** 
BNYS Final Year Student | Tech Enthusiast | Founder of Praneon
📧 Email: vishal@praneon.com
💼 LinkedIn: https://www.linkedin.com/in/drvishaln/
🌐 Website: https://praneon.com

---

