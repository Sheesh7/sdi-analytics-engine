import sqlite3
import random
from datetime import datetime, timedelta

DB_PATH = "db/soccer_analytics.db"


TEAMS = [
    (1, "Brazil", "G", "CONMEBOL"),
    (2, "France", "D", "UEFA"),
    (3, "Argentina", "C", "CONMEBOL"),
    (4, "Germany", "E", "UEFA")
]

def create_connection():
    return sqlite3.connect(DB_PATH)

def generate_teams(cursor):
    cursor.executemany(
        "INSERT INTO teams VALUES (?, ?, ?, ?)",
        TEAMS
    )

def generate_player_logs(cursor):
    start_date = datetime.now() - timedelta(days=45)
    player_id = 1
    for team_id, _, _, _ in TEAMS:
        for _ in range(11):
            match_date = start_date
            fatigue = random.uniform(.1,.3)
            while match_date < datetime.now():
                minutes = random.choice([60,75,90])
                distance = round(random.uniform(7.5, 12.5), 2)
                avg_speed = round(random.uniform(6.5, 8.5), 2)
                sprints = random.randint(10,35)
                fatigue += (minutes / 90) * .05
                cursor.execute(
                    """
                    INSERT INTO player_logs
                    (player_id, team_id, match_date, minutes_played, distance_km, avg_speed, sprint_count, fatigue_index)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        player_id, team_id, match_date.date(), minutes, distance, avg_speed, sprints, fatigue
                    )
                )
                match_date += timedelta(days=5)
            player_id += 1

def generate_injuries(cursor):
    injuries = [
        (3, "2025-07-02", "Hamstring", 1),
        (12, "2025-07-10", "Ankle", 1),
        (25, "2025-07-15", "Knee", 0)
    ]
    cursor.executemany(
        """
        INSERT INTO injury_events
        (player_id, event_date, injury_type, resolved)
        VALUES (?, ?, ?, ?)
        """,
        injuries
    )

def main():
    conn = create_connection()
    cursor = conn.cursor()

    with open("db/schema.sql", "r") as f:
        cursor.executescript(f.read())
    generate_teams(cursor)
    generate_player_logs(cursor)
    generate_injuries(cursor)
    conn.commit()
    conn.close()
    print("Soccer Analytics Dataset created.")
if __name__ == "__main__":
    main()