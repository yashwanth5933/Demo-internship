from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__, template_folder="../templates")

data = {
    "area":[500,600,700,800,900],
    "bedrooms":[2,3,3,4,4],
    "bathrooms":[1,2,2,3,3],
    "price":[200000,250000,300000,350000,400000]
}

df = pd.DataFrame(data)

X = df[['area','bedrooms','bathrooms']]
y = df['price']

model = LinearRegression()
model.fit(X,y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    area=float(request.form["area"])
    bedrooms=float(request.form["bedrooms"])
    bathrooms=float(request.form["bathrooms"])

    prediction=model.predict([[area,bedrooms,bathrooms]])

    return f"Predicted Price: {prediction[0]}"

app = app
