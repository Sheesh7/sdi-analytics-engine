import pandas as pd
from utils.db_connection import get_connection

def load_fatigue_kpis(conn):
    query = """
        SELECT
            player_id,
            team_id,
            as_of_date,
            matches_last_14_days,
            minutes_last_14_days,
            avg_fatigue_index,
            fatigue_score
        FROM player_fatigue_kpis;
    """
    return pd.read_sql(query, conn)

def load_alerts(conn):
    query = """
        SELECT
            player_id,
            severity,
            status
        FROM alerts
        WHERE status = 'OPEN';
    """
    return pd.read_sql(query, conn)

def load_teams(conn):
    query = """
        SELECT
            team_id,
            team_name
        FROM teams;
    """
    return pd.read_sql(query, conn)

def team_fatigue_summary(fatigue_df, teams_df):
    team_summary = (
        fatigue_df
        .groupby("team_id")
        .agg(
            avg_fatigue_score=("fatigue_score", "mean"),
            avg_minutes=("minutes_last_14_days", "mean"),
            players_tracked=("player_id", "nunique")
        )
        .reset_index()
    )
    return team_summary.merge(teams_df, on="team_id")

def high_risk_players(fatigue_df, threshold=65):
    return fatigue_df[fatigue_df["fatigue_score"] >= threshold] \
            .sort_values("fatigue_score", ascending=False)

def alert_counts_by_team(alerts_df, fatigue_df, teams_df):
    merged = alerts_df.merge(
        fatigue_df[["player_id", "team_id"]],
        on="player_id",
        how="left"
    )
    alert_counts = (
        merged
        .groupby("team_id")
        .size()
        .reset_index(name="open_alerts")
    )
    return alert_counts.merge(teams_df, on="team_id", how="left")


def main():
    conn = get_connection()
    fatigue_df = load_fatigue_kpis(conn)
    alerts_df = load_alerts(conn)
    teams_df = load_teams(conn)
    conn.close()
    team_summary = team_fatigue_summary(fatigue_df, teams_df)
    risky_players = high_risk_players(fatigue_df)
    alerts_by_team = alert_counts_by_team(alerts_df, fatigue_df, teams_df)
    print("\n=== TEAM FATIGUE SUMMARY ===")
    print(team_summary.sort_values("avg_fatigue_score", ascending=False))
    print("\n=== HIGH RISK PLAYERS (Fatigue >= 65) ===")
    print(risky_players[["player_id", "team_id", "fatigue_score"]].head(10))
    print("\n=== OPEN ALERTS BY TEAM ===")
    print(alerts_by_team.sort_values("open_alerts", ascending=False))

if __name__ == "__main__":
    main()