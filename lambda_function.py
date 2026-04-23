import json
import os
from pathlib import Path
from typing import Any

from utils.analytics import (
    load_data,
    calculate_kpis,
    detect_anomalies,
    machine_summary,
)


def build_result_from_csv(csv_path: str | Path) -> dict[str, Any]:
    """
    Read a CSV file, process the data, and return a JSON-serializable result.
    """
    df = load_data(str(csv_path))

    kpis = calculate_kpis(df)

    anomalies_df = detect_anomalies(df).copy()
    anomalies_df["timestamp"] = anomalies_df["timestamp"].astype(str)
    anomalies = anomalies_df.to_dict(orient="records")

    summary_df = machine_summary(df).copy()
    summary = summary_df.to_dict(orient="records")

    recent_df = df.tail(5).copy()
    recent_df["timestamp"] = recent_df["timestamp"].astype(str)
    recent_data = recent_df.to_dict(orient="records")

    return {
        "kpis": kpis,
        "anomalies": anomalies,
        "summary": summary,
        "recent_data": recent_data,
    }


def save_result_json(result: dict[str, Any], output_path: str | Path) -> None:
    """
    Save processed result to a JSON file.
    """
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """
    AWS Lambda entry point.

    For the first local version, this handler supports a simple event shape:
    {
        "input_csv": "data/production_data.csv",
        "output_json": "data/result.json"
    }

    Later, this can be extended to handle S3 trigger events.
    """
    input_csv = event.get("input_csv", "data/production_data.csv")
    output_json = event.get("output_json", "data/result.json")

    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Input CSV file not found: {input_csv}")

    result = build_result_from_csv(input_csv)
    save_result_json(result, output_json)

    return {
        "statusCode": 200,
        "message": "Processing completed successfully.",
        "input_csv": input_csv,
        "output_json": output_json,
    }


if __name__ == "__main__":
    # Local test mode: simulate a Lambda invocation
    test_event = {
        "input_csv": "data/production_data.csv",
        "output_json": "data/result.json",
    }

    response = lambda_handler(test_event, None)
    print(json.dumps(response, indent=2))