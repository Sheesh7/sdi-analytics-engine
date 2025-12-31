DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS alerts;
DROP TABLE IF EXISTS injury_events;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS player_logs;
DROP TABLE IF EXISTS player_fatigue_kpis;
DROP TABLE IF EXISTS fatigue_anomalies;
DROP TABLE IF EXISTS fatigue_predictions;

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT, 
    group_name TEXT,
    confederation TEXT
);
CREATE TABLE player_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    team_id INTEGER,
    match_date DATE,
    minutes_played INTEGER,
    distance_km REAL,
    avg_speed REAL, 
    sprint_count INTEGER,
    fatigue_index REAL,
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);
CREATE table injury_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    event_date DATE, 
    injury_type TEXT,
    resolved INTEGER
);
CREATE TABLE alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    created_at DATETIME,
    severity TEXT,
    reason TEXT,
    status TEXT
);
CREATE TABLE player_fatigue_kpis (
    player_id INTEGER,
    team_id INTEGER,
    as_of_date TEXT,
    matches_last_14_days INTEGER,
    minutes_last_14_days INTEGER,
    avg_fatigue_index REAL,
    fatigue_score REAL
);
CREATE TABLE fatigue_anomalies (
    anomaly_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    team_id INTEGER,
    as_of_date TEXT,
    fatigue_score REAL,
    z_score REAL,
    anomaly_flag INTEGER
);
CREATE TABLE fatigue_predictions(
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    team_id INTEGER,
    as_of_date DATE,
    predicted_injury_risk TEXT,
    confidence REAL
);