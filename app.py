from flask import Flask, render_template, request
from model import predict_fruit, predict_house

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    area = float(request.form['area'])
    rooms = float(request.form['rooms'])
    age = float(request.form['age'])

    price = predict_house(area, rooms, age)

    f1 = float(request.form['f1'])
    f2 = float(request.form['f2'])
    f3 = float(request.form['f3'])
    f4 = float(request.form['f4'])

    fruit = predict_fruit([f1,f2,f3,f4])

    return render_template('index.html',
                           price=price,
                           fruit=fruit)

if __name__ == '__main__':
    app.run(debug=True)
