from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def collect_metrics():
    pass


def process_metrics():
    pass


def detect_anomaly():
    pass


def generate_report():
    pass


with DAG(
    dag_id="health_monitor_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    collect_metrics_task = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics,
    )
    process_metrics_task = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics,
    )
    detect_anomaly_task = PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly,
    )
    generate_report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    collect_metrics_task >> process_metrics_task >> detect_anomaly_task >> generate_report_task
