from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and preprocessor
model = pickle.load(open("artifacts/model.pkl", "rb"))
preprocessor = pickle.load(open("artifacts/preprocessor.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = request.form["gender"]
    race = request.form["race"]
    reading_score = float(request.form["reading_score"])
    writing_score = float(request.form["writing_score"])

    # Temporary values for remaining features
    data = pd.DataFrame([{
        "gender": gender,
        "race/ethnicity": race,
        "parental level of education": "bachelor's degree",
        "lunch": "standard",
        "test preparation course": "none",
        "reading score": reading_score,
        "writing score": writing_score
    }])

    data_processed = preprocessor.transform(data)

    prediction = model.predict(data_processed)[0]

    prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Math Score: {prediction}"
    )


if __name__ == "__main__":
    app.run(debug=True)