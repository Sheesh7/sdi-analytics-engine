# Soccer Fatigue Analytics Engine

A modular analytics pipeline that simulates, processes, and analyzes player workload data to detect fatigue risk, anomalies, and injury likelihood.

## 🚀 Features
- Synthetic soccer performance data generation
- Rolling 14-day fatigue KPIs
- Rule-based injury risk predictions
- Automated alert generation
- Fatigue anomaly detection
- End-to-end pipeline orchestration

## 🧱 Project Architecture
sdi-analytics-engine/
|
|-- analytics/ 
|-- |-- ingest.py # Load data from SQLite
|-- |-- fatigue.py # Compute fatigue KPIs
|-- |-- alerts.py # Generate fatigue-based alerts
|-- |-- kpis.py # Team & system-level KPIs
|-- |-- anomaly_detection.py # Detect fatigue anomalies
|-- |-- prediction.py # Predict injury risk
|
|-- data/
|-- |-- generate_data.py # Synthetic data generator
|
|-- db/
|-- |-- schema.sql # Database schema
|-- |-- soccer_analytics.db # SQLite database
|
| utils/
|-- |-- db_connection.py # Shared database connection
|-- |-- logger.py # Centralized logging
|
|-- main.py # Pipeline orchestrator
|-- requirements.txt
|-- README.md

## 🔄 Pipeline Flow
1. Generate synthetic data
2. Ingest data in SQLite
3. Compute fatigue KPIs
4. Detect anomalies
5. Generate alerts
6. Predict injury risk

## 📊 Key Analytics Logic
# Fatigue KPIs
Fatigue is computed using a rolling 14-day window per player
- Matches played
- Total minutes
- Average fatigue index
- Composite fatigue score
# Alerts
Alerts are triggered based on:
- High fatigue score thresholds
- Overplayed minutes
- Combination of unresolved injuries and fatigue
# Anomaly Detection
Detects abnormal ftigue spikes using z-score deviation from player baselines
# Injury Risk Prediction
Rule-based model that classifies injury risk as:
- Low
- Medium
- High
Each prediction includes a confidence score

## ▶️ How to Run
# Install dependencies
pip install -r requirements.txt
# Intialize database & generate data
python data/generate_data.py
# Run full pipeline
python main.py

## 🛠 Tech Stack
- Python
- SQLite
- Pandas
- Modular Analytics Design

## 📌 Use Cases
- Sports analytics & performance monitoring
- Injury prevention modeling
- Data engineering pipeline demonstrations

## 📈 Future Improvements
- Replace rule-based prediction with ML models
- Add REST API layer
- Dashboard visulaization (Tableau|Power BI|StreamLit)
- Multi-league & season support

👤 Author
Built by Yashish Eriki
Data Science & Analytics Enthusiast

⭐ Why This Project Matters
This project demonstrates:
- Clean data pipeine architecture
- Analytical reasoning
- End-to-end system thinking
- Real-world sports analytics use cases