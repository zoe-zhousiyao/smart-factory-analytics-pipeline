import json
import os
from flask import Flask, render_template

app = Flask(__name__)


def load_processed_result(json_path: str = "data/result.json") -> dict:
    """
    Load precomputed analytics result from a JSON file.
    """
    if not os.path.exists(json_path):
        raise FileNotFoundError(
            f"Processed result file not found: {json_path}. "
            "Please run lambda_function.py first to generate data/result.json."
        )

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def dashboard():
    result = load_processed_result("data/result.json")

    return render_template(
        "index.html",
        kpis=result["kpis"],
        anomalies=result["anomalies"],
        summary=result["summary"],
        recent_data=result["recent_data"],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)