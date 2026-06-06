from src.loader import load_data
from src.profiler import profile_dataset
from src.risk_scoring import calculate_risk_scores
from src.report_generator import generate_report

from src.analyzer import (
    threat_summary,
    top_attacker_ips,
    blocked_ips,
    detect_security_tools
)

from src.visualizer import (
    threat_distribution,
    protocol_distribution,
    top_risk_ips_chart
)

FILE_PATH = "data/cybersecurity_threat_detection_logs.csv"


def main():

    df = load_data(FILE_PATH)

    if df is not None:

        profile_dataset(df)

        threat_counts = threat_summary(df)

        attackers = top_attacker_ips(df)

        blocked = blocked_ips(df)

        detect_security_tools(df)

        risk_table = calculate_risk_scores(df)

        threat_distribution(df)

        protocol_distribution(df)

        top_risk_ips_chart(risk_table)

        generate_report(
            df,
            threat_counts,
            attackers,
            blocked,
            risk_table
        )


if __name__ == "__main__":
    main()