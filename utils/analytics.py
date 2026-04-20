import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def calculate_kpis(df: pd.DataFrame) -> dict:
    total_output = int(df["output_units"].sum())
    total_defects = int(df["defect_units"].sum())
    avg_temperature = round(df["temperature"].mean(), 2)
    total_downtime = int(df["downtime_min"].sum())

    defect_rate = round((total_defects / total_output) * 100, 2) if total_output else 0

    return {
        "total_output": total_output,
        "total_defects": total_defects,
        "defect_rate": defect_rate,
        "avg_temperature": avg_temperature,
        "total_downtime": total_downtime,
    }


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    anomalies = df[
        (df["temperature"] > 80) |
        (df["defect_units"] >= 8) |
        (df["downtime_min"] >= 15)
    ].copy()
    return anomalies


def machine_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby("machine_id").agg({
        "output_units": "sum",
        "defect_units": "sum",
        "temperature": "mean",
        "downtime_min": "sum"
    }).reset_index()

    summary["defect_rate"] = round(
        (summary["defect_units"] / summary["output_units"]) * 100, 2
    )
    summary["temperature"] = summary["temperature"].round(2)

    return summary