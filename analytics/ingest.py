import pandas as pd
from utils.db_connection import get_connection


def load_teams(conn):
    """
    Load players table into a pandas DataFrame.
    """
    query = """
        SELECT
            team_id,
            team_name,
            group_name,
            confederation
        FROM teams
    """
    return pd.read_sql(query, conn)

def load_player_logs(conn):
    """
    Load matches table into a pandas DataFrame.
    """
    query = """
        SELECT
            player_id,
            team_id,
            match_date, 
            minutes_played,
            distance_km,
            avg_speed,
            sprint_count,
            fatigue_index
        FROM player_logs;
    """
    return pd.read_sql(query, conn)

def load_injuries(conn):
    """
    Load player match-level stats into a pandas DataFrame.
    """
    query = """
        SELECT
            player_id,
            event_date,
            injury_type,
            resolved
        FROM injury_events;
    """
    return pd.read_sql(query, conn)

def main():
    """
    Entry point for data ingestion
    """
    conn = get_connection()
    teams_df = load_teams(conn)
    logs_df = load_player_logs(conn)
    injuries_df = load_injuries(conn)

    conn.close()

    print("Teams loaded:", len(teams_df))
    print("Player Logs loaded:", len(logs_df))
    print("Injuries loaded:", len(injuries_df))

    print("\n Sample Player Logs:")
    print(logs_df)

    print("\nSample Injuries:")
    print(injuries_df.head())

if __name__ == "__main__":
    main()

