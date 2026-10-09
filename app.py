from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model/rent_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "BHK": float(request.form["BHK"]),
        "Size": float(request.form["Size"]),
        "Floor": request.form["Floor"],
        "Area_Type": request.form["Area_Type"],
        "Area_Locality": request.form["Area_Locality"],
        "City": request.form["City"],
        "Furnishing_Status": request.form["Furnishing_Status"],
        "Tenant_Preferred": request.form["Tenant_Preferred"],
        "Bathroom": float(request.form["Bathroom"]),
        "Point_of_Contact": request.form["Point_of_Contact"]
    }

    input_data = pd.DataFrame([data])

    print("Input Data:")
    print(input_data)

    prediction = model.predict(input_data)[0]

    return render_template(
        "result.html",
        prediction=round(prediction)
    )


if __name__ == "__main__":
    app.run(debug=True)