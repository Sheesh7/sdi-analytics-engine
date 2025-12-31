import pandas as pd
from datetime import datetime
from utils.db_connection import get_connection

def load_fatigue_kpis(conn):
    query = """
        SELECT
            player_id,
            team_id,
            as_of_date,
            fatigue_score
        FROM player_fatigue_kpis;
    """
    df = pd.read_sql(query, conn)
    df["as_of_date"] = pd.to_datetime(df["as_of_date"])
    return df

def predict_fatigue(df, window=3):
    predictions = []
    for _, row in df.iterrows():
        score = row["fatigue_score"]
        if score >= 55:
            risk = "HIGH"
        elif score >= 40:
            risk = "MEDIUM"
        else:
            risk = "LOW"
        predictions.append({
            "player_id" : row["player_id"],
            "team_id" : row["team_id"],
            "as_of_date" : row["as_of_date"],
            "predicted_injury_risk" : risk,
            "confidence" : round(min(score / 60, .95), 2)
        })
    return pd.DataFrame(predictions)

def clear_predictions(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fatigue_predictions;")
    conn.commit()

def write_predictions(conn, df):
    df.to_sql(
        "fatigue_predictions",
        conn,
        if_exists="append",
        index=False
    )

def main():
    conn = get_connection()
    fatigue_df = load_fatigue_kpis(conn)
    predictions_df = predict_fatigue(fatigue_df)
    clear_predictions(conn)
    write_predictions(conn, predictions_df)
    conn.close()
    print("Predictions generated:", len(predictions_df))
    print("\nSample Predictions:")
    print(predictions_df.head(12))

if __name__ == "__main__":
    main()