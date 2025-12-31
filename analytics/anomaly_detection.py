import pandas as pd
from datetime import datetime
from utils.db_connection import get_connection


def load_fatigue_data(conn):
    query = """
        SELECT
            player_id,
            as_of_date,
            fatigue_score
        FROM player_fatigue_kpis
        ORDER BY player_id, as_of_date;
    """
    return pd.read_sql(query, conn)

def detect_anomalies(df):
    anomalies = []
    for player_id, group in df.groupby("player_id"):
        group = group.sort_values("as_of_date")
        group["fatigue_delta"] = group["fatigue_score"].diff()

        for _, row in group.iterrows():
            if row["fatigue_delta"] is not None and row["fatigue_delta"] > 15:
                anomalies.append({
                    "player_id" : player_id,
                    "as_of_date" : row["as_of_date"],
                    "fatigue_score" : row["fatigue_score"],
                    "fatigue_jump" : round(row["fatigue_delta"], 2),
                    "anomaly_type" : "SUDDEN_FATIGUE_SPIKE"
                })
    return pd.DataFrame(anomalies)

def main():
    conn = get_connection()
    fatigue_df =  load_fatigue_data(conn)
    anomalies_df = detect_anomalies(fatigue_df)
    conn.close()

    print("Anomalies detected:", len(anomalies_df))
    print("\nSample Anomalies:")
    print(anomalies_df.head(10))

if __name__ == "__main__":
    main()

