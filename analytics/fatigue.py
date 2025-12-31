import pandas as pd
from datetime import timedelta
from utils.db_connection import get_connection

def load_player_logs(conn):
    query = """
        SELECT
            player_id,
            team_id, 
            match_date,
            minutes_played,
            fatigue_index
        FROM player_logs;
    """
    df = pd.read_sql(query, conn)
    df["match_date"] = pd.to_datetime(df["match_date"])
    return df

def calculate_fatigue(df):
    results = []
    for player_id, group in df.groupby("player_id"):
        group = group.sort_values("match_date")
        team_id = group["team_id"].iloc[0]

        for current_date in group["match_date"].unique():
            window_start = current_date - timedelta(days=14)
            window = group[
                (group["match_date"] >= window_start) &
                (group["match_date"] <= current_date)
            ]
            matches = len(window)
            minutes = window["minutes_played"].sum()
            avg_fatigue = window["fatigue_index"].mean()

            fatigue_score = (
                (minutes / 90) * .5 + matches * 5 + avg_fatigue * 100
            )
            results.append({
                "player_id": player_id,
                "team_id": team_id,
                "as_of_date": current_date.date().isoformat(),
                "matches_last_14_days": matches,
                "minutes_last_14_days": minutes,
                "avg_fatigue_index": round(avg_fatigue, 3),
                "fatigue_score": round(fatigue_score, 2)
            })
    return pd.DataFrame(results)

def write_kpis(conn, df):
    df.to_sql(
        "player_fatigue_kpis",
        conn,
        if_exists="append",
        index=False
    )

def main():
    conn = get_connection()
    logs_df = load_player_logs(conn)
    fatigue_df = calculate_fatigue(logs_df)
    write_kpis(conn, fatigue_df)
    conn.close()
    print("Fatigue KPIs generated:", len(fatigue_df))
    print("\nSample Fatigue KPIs:")
    print(fatigue_df.head())

if __name__ == "__main__":
    main()