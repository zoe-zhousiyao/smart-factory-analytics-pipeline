from flask import Flask, render_template
from utils.analytics import load_data, calculate_kpis, detect_anomalies, machine_summary

app = Flask(__name__)


@app.route("/")
def dashboard():
    df = load_data("data/production_data.csv")

    kpis = calculate_kpis(df)
    anomalies = detect_anomalies(df)
    summary = machine_summary(df)

    return render_template(
        "index.html",
        kpis=kpis,
        anomalies=anomalies.to_dict(orient="records"),
        summary=summary.to_dict(orient="records"),
        recent_data=df.tail(5).to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)