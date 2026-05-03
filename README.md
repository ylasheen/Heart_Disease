# ❤️ Heart Disease Prediction Project

## 📋 Overview
This project predicts the likelihood of a person having heart disease using Artificial Intelligence and Machine Learning techniques.  
The workflow includes:
- Data cleaning and preprocessing  
- Feature selection  
- Model training  
- Model evaluation  
- A Streamlit web interface for easy prediction.

---

## 🏗 Project Structure
Heart_Disease_Project/
├── data/                  # Raw and cleaned data
│   ├── heart_disease.csv
│   └── heart_disease_clean.csv
├── models/                # Saved final model
│   └── final_model.pkl
├── notebooks/             # Jupyter notebooks for each step
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_selection.ipynb
│   ├── 03_supervised_learning.ipynb
│   ├── 04_hyperparameter_tuning.ipynb
│   └── 05_results_analysis.ipynb
├── results/               # Model evaluation outputs
│   ├── evaluation_metrics.txt
│   ├── predictions_test.csv
│   ├── roc_curve.png
│   └── confusion_matrix.png
├── app.py                 # Streamlit web app
└── requirements.txt       # Project dependencies

---

## ⚙️ Requirements
- Python 3.10 or higher  
- Install all dependencies:
pip install -r requirements.txt

---

## 🚀 How to Run
1. Open a terminal inside the project folder.  
2. (Optional) Activate your virtual environment.  
3. Install the requirements:
   
   pip install -r requirements.txt
   
4. Run the Streamlit web app:
   
   streamlit run app.py
   
5. Open the browser at the URL shown in the terminal (usually http://localhost:8501).

---

## 📊 Model Results
- Best Model: Logistic Regression  
- Accuracy: ~0.87  
- ROC-AUC: ~0.93  
- Top Features: thalach, cp, ca, thal, oldpeak

---
Developed by youssef lasheen

📧 Email: ylasheen53@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/youssef-lasheen-1b4652295

🖥 GitHub: https://github.com/ylasheen