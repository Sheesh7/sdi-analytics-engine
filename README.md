# Soccer Fatigue Analytics Engine

A modular analytics pipeline that simulates, processes, and analyzes player workload data to detect fatigue risk, anomalies, and injury likelihood.

## 🚀 Features
- Synthetic soccer performance data generation
- Rolling 14-day fatigue KPIs
- Rule-based injury risk predictions
- Automated alert generation
- Fatigue anomaly detection
- End-to-end pipeline orchestration

## 🧱 Project Structure
sdi-analytics-engine  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;analytics  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ingest.py              # Load data from SQLite  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fatigue.py             # Compute fatigue KPIs  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;alerts.py              # Generate fatigue-based alerts  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kpis.py                # Team & system-level KPIs  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;anomaly_detection.py   # Detect fatigue anomalies  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prediction.py          # Predict injury risk  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;generate_data.py       # Synthetic data generator  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;db  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;schema.sql             # Database schema  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;soccer_analytics.db    # SQLite database  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;utils  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;db_connection.py       # Shared database connection  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logger.py              # Centralized logging  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main.py                  # Pipeline orchestrator  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requirements.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;README.md  


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

# 👤 Author
Built by Yashish Eriki
Data Science & Analytics Enthusiast

# ⭐ Why This Project Matters
This project demonstrates:
- Clean data pipeine architecture
- Analytical reasoning
- End-to-end system thinking
- Real-world sports analytics use cases
