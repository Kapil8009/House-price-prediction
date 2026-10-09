# 🏠 House Rent Prediction Using Machine Learning

## 📌 Project Overview

The **House Rent Prediction** project is a machine learning web application built using Python and Flask. It predicts the estimated monthly rent of a house based on user-provided property details, such as the number of bedrooms, property size, floor, location, city, furnishing status, and other relevant features.

The application uses a trained machine learning model to generate rent predictions through a simple web interface.

Real time Prject Link Project - https://house-price-prediction-esc9.onrender.com/


## ✨ Features

* Predict house rent based on property details.
* User-friendly web interface built with Flask and HTML templates.
* Machine learning model integration using Joblib.
* Data handling and preprocessing using Pandas.
* Supports multiple property-related features.
* Displays the predicted rent on a result page.

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Flask** — Web application framework
* **Pandas** — Data manipulation and processing
* **Scikit-learn** — Machine learning model development (if used to train the model)
* **Joblib** — Loading the trained model
* **HTML/CSS** — Frontend interface
* **Git and GitHub** — Version control and project hosting

## 📂 Project Structure

```text
house-rent-prediction/
│
├── app.py
├── model/
│   └── rent_model.pkl
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── README.md
```

## 📋 Input Features

The model uses the following features to predict house rent:

| Feature           | Description                                |
| ----------------- | ------------------------------------------ |
| BHK               | Number of bedrooms, halls, and kitchens    |
| Size              | Property size, typically in square feet    |
| Floor             | Floor on which the property is located     |
| Area_Type         | Type of area measurement or classification |
| Area_Locality     | Locality of the property                   |
| City              | City where the property is located         |
| Furnishing_Status | Furnishing condition of the property       |
| Tenant_Preferred  | Preferred tenant category                  |
| Bathroom          | Number of bathrooms                        |
| Point_of_Contact  | Contact or listing category                |

**Note:** The input values and their formats must match the features and preprocessing used when training the machine learning model.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kapil8009/House-price-prediction.git
```

### 2. Navigate to the project directory

```bash
cd House-price-prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Linux or Kali Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the main dependencies:

```bash
pip install flask pandas joblib scikit-learn
```

### 5. Run the application

```bash
python app.py
```

### 6. Open the application

Open your browser and visit:

http://127.0.0.1:5000/

Enter the property details in the form and submit them to view the predicted rent.

## 🔍 How It Works

1. The user opens the home page.
2. The user enters property details into the prediction form.
3. Flask receives the submitted form data.
4. The application converts numerical inputs and creates a Pandas DataFrame.
5. The trained model (`rent_model.pkl`) processes the input features.
6. The model predicts the estimated rent.
7. Flask displays the prediction on the result page.

## 🧠 Machine Learning Model

The trained model is loaded using Joblib:

```python
model = joblib.load("model/rent_model.pkl")
```

Predictions are generated using:

```python
prediction = model.predict(input_data)[0]
```

The predicted value is rounded before being displayed to the user.

The model's accuracy and performance depend on the training dataset, selected algorithm, preprocessing steps, and evaluation metrics.

## 🚀 Future Improvements

* Add data validation and user-friendly error messages.
* Improve the user interface with responsive CSS and Bootstrap.
* Display rent estimates with the appropriate currency.
* Evaluate model performance using metrics such as MAE, RMSE, and R².
* Add visualizations to explore rental prices by city and locality.
* Deploy the application using a suitable cloud hosting platform.
* Add automated tests for prediction routes and input validation.

## ⚠️ Important Notes

* The trained model file must exist at `model/rent_model.pkl`.
* The `templates` directory must contain `index.html` and `result.html`.
* The feature names and order must be consistent with the model's training pipeline.
* Run the application locally for development. Disable Flask debug mode when deploying publicly.
* Predictions are estimates and should not be treated as guaranteed market prices.

## 👨‍💻 Author

**Kapil**

GitHub: [Kapil8009](https://github.com/Kapil8009)

## 📄 License

This project is available for educational and learning purposes. Add a specific open-source license, such as the MIT License, if you intend to distribute it under those terms.
