from flask import Flask, render_template, request
from cypp import *


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        user_input = get_user_input(request.form)
        input_keys = list(user_input.keys())
        input_values = list(user_input.values())
        yield_value, future_income = get_predictions(user_input)
    return render_template("submit.html", input_keys=input_keys, input_values=input_values, yield_value=yield_value, future_income=future_income)


if __name__ == "__main__":
    app.run(debug=True)
