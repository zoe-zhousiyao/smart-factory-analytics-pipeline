# smart-factory-analytics-pipeline
A cloud-ready data analytics pipeline for manufacturing data. The system ingests production records, processes them with Python, stores structured data in SQLite/CSV, detects anomalies, and serves results through a Flask web dashboard. Designed to be deployable with Docker and extendable to AWS services such as S3, Lambda, and EC2.

# Smart Factory Analytics Pipeline

A cloud-ready data analytics pipeline for manufacturing data, built with Python and Flask.  
This project simulates a real-world production environment where data is processed, analyzed, and visualized to support data-driven decision-making.

---

## 🚀 Overview

This project demonstrates how production data can be transformed into actionable insights through a data pipeline.

It includes:
- Data ingestion from CSV (simulating factory systems)
- Data processing and KPI calculation
- Anomaly detection
- Machine-level performance analysis
- Web-based dashboard for visualization
- Docker-based deployment

The architecture is designed to be easily extendable to cloud platforms such as AWS.

---

## 🧠 Key Features

- 📊 **Production KPI Dashboard**
  - Total output
  - Defect rate
  - Average temperature
  - Downtime analysis

- 🏭 **Machine-Level Analytics**
  - Performance per machine
  - Defect rate comparison
  - Temperature and downtime metrics

- ⚠️ **Anomaly Detection**
  - Identifies abnormal production conditions:
    - High temperature
    - High defect rate
    - High downtime

- 📈 **Recent Data Monitoring**
  - Displays latest production records

- 🐳 **Containerized Deployment**
  - Fully dockerized application

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Data Processing**: Pandas
- **Frontend**: HTML, CSS (Jinja2 Templates)
- **Deployment**: Docker
- **Version Control**: Git & GitHub

---

## 🏗️ Project Structure
