import pandas as pd
from datetime import datetime
from utils.db_connection import get_connection


def load_fatigue_kpis(conn):
    query = """
        SELECT
            player_id,
            team_id, 
            as_of_date,
            matches_last_14_days,
            minutes_last_14_days,
            fatigue_score
        FROM player_fatigue_kpis;
    """
    return pd.read_sql(query, conn)

def load_unresolved_injuries(conn):
    query = """
        SELECT DISTINCT player_id
        FROM injury_events
        WHERE resolved = 0;
    """
    return pd.read_sql(query, conn)

def generate_alerts(fatigue_df, injuries_df):
    alerts = []
    injured_players = set(injuries_df["player_id"])
    for _, row in fatigue_df.iterrows():
        player_id = row["player_id"]
        fatigue = row["fatigue_score"]
        minutes = row["minutes_last_14_days"]
        severity = None
        reason = None
        if fatigue >= 80:
            severity = "CRITICAL"
            reason = "Extreme fatigue level"
        elif fatigue >= 65:
            severity = "HIGH"
            reason = "High fatigue level"
        elif minutes >= 300:
            severity = "WARNING"
            reason = "Overplayed in last 14 days"
        if player_id in injured_players and fatigue >= 65:
            severity = "CRITICAL"
            reason = "High fatigue with unresolved injury"
        if severity:
            alerts.append((
                player_id,
                datetime.now(),
                severity,
                reason,
                "OPEN"
            ))
    return alerts

def insert_alerts(conn, alerts):
    if not alerts:
        return
    
    cursor = conn.cursor()
    cursor.executemany(
        """
        INSERT INTO alerts
        (player_id, created_at, severity, reason, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        alerts
    )
    conn.commit()

def main():
    conn = get_connection()
    fatigue_df = load_fatigue_kpis(conn)
    injuries_df = load_unresolved_injuries(conn)
    alerts = generate_alerts(fatigue_df, injuries_df)
    insert_alerts(conn, alerts)
    conn.close()
    print(f"Alerts generated: {len(alerts)}")

if __name__ == "__main__":
    main()