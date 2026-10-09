from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    symbol = request.form.get("symbol")
    expiry = request.form.get("expiry")
    uploaded_file = request.files.get("file")

    if uploaded_file:
        df = pd.read_csv(uploaded_file, encoding="latin1")

        print("Symbol:", symbol)
        print("Expiry:", expiry)
        print(df)

        return render_template(
            "result.html",
            symbol=symbol,
            expiry=expiry,
            data=df.to_html(classes="data-table", index=False)
        )

    return "No file uploaded"


if __name__ == "__main__":
    app.run(debug=Trgithttps://github.com/Satwik-lab/Option-Chain-Snapshot-Analyser.git