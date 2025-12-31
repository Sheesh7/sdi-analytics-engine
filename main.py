from analytics.ingest import main as ingest_main
from analytics.fatigue import main as fatigue_main
from analytics.kpis import main as kpis_main
from analytics.anomaly_detection import main as anomaly_detection_main
from analytics.prediction import main as prediction_main
from analytics.alerts import main as alerts_main
from utils.logger import setup_logger

logger = setup_logger("MAIN")

def run_pipeline():
    logger.info("Starting SDI Analytics Engine pipeline")

    ingest_main()
    logger.info("Ingestion comlete")

    fatigue_main()
    logger.info("Fatigue KPIs complete")

    kpis_main()
    logger.info("Team KPIs complete")

    anomaly_detection_main()
    logger.info("Anomaly detection complete")

    prediction_main()
    logger.info("Injury prediction complete")

    alerts_main()
    logger.info("Alerts generation complete")

    logger.info("Pipeline finished successfully")

if __name__ == "__main__":
    run_pipeline()
