from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("loan_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = int(request.form["gender"])
    married = int(request.form["married"])
    dependents = int(request.form["dependents"])
    education = int(request.form["education"])
    self_employed = int(request.form["self_employed"])
    applicant_income = float(request.form["applicant_income"])
    coapplicant_income = float(request.form["coapplicant_income"])
    loan_amount = float(request.form["loan_amount"])
    loan_term = float(request.form["loan_term"])
    credit_history = float(request.form["credit_history"])
    property_area = int(request.form["property_area"])

    sample = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    prediction = model.predict(sample)

    prediction = model.predict(sample)

    probability = model.predict_proba(sample)

    confidence = round(max(probability[0]) * 100, 2)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence
    )
if __name__ == "__main__":
    app.run(debug=True)