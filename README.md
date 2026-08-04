# 🏦 LOAN APPROVAL PREDICTION USING MACHINE LEARNING

A Machine Learning-based web application that predicts whether a loan application is **Approved** or **Rejected** based on applicant information. The model is built using the **Random Forest Classifier** and deployed using the **Flask** framework with an interactive web interface.

---

## 📌 Project Overview

Loan approval is a crucial process in the banking sector. Evaluating every loan application manually is time-consuming and may lead to inconsistencies. This project automates the loan approval process using Machine Learning by analyzing applicant details such as income, education, credit history, loan amount, and property area.

The trained model is integrated into a Flask web application where users can enter applicant information and instantly receive the loan approval prediction along with the model's confidence score.

---

## ✨ Features

- Loan Approval Prediction
- Interactive Web Interface
- Random Forest Machine Learning Model
- Hyperparameter Tuning using GridSearchCV
- Prediction Confidence Score
- Responsive UI using HTML & CSS
- Fast and User-Friendly

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Random Forest Classifier
- GridSearchCV
- Scikit-learn

### Libraries
- Pandas
- NumPy
- Joblib
- Matplotlib
- Seaborn

### Web Technologies
- Flask
- HTML
- CSS
- JavaScript

### Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```
Loan-Approval-Prediction/
│
├── app.py
├── Loan Prediction.ipynb
├── loan_data.csv
├── loan_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 📊 Input Features

The model predicts loan approval based on the following features:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

### Output

- ✅ Loan Approved
- ❌ Loan Rejected

---

## ⚙️ Project Workflow

```
Dataset
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Encoding
      ↓
Random Forest Model Training
      ↓
GridSearchCV Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Save Model (.pkl)
      ↓
Flask Web Application
      ↓
Loan Prediction
```

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | Random Forest Classifier |
| Accuracy | 78.04% |

---

## ▶️ Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Mohammadsameera3/Loan-Approval-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Loan-Approval-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 📷 Application Preview

The web application allows users to:

- Enter applicant details
- Predict loan approval status
- View the confidence score
- Get instant results

---

## 🎯 Future Enhancements

- Deploy the application on Render or Railway
- Connect with a database
- Add user authentication
- Generate downloadable loan eligibility reports
- Improve prediction accuracy using advanced machine learning models

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning Model Development
- Hyperparameter Tuning
- Flask Web Development
- Frontend Development
- Git & GitHub

---

## 👨‍💻 Author

**Mohammad Sameera**
