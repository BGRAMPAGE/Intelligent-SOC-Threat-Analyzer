from datetime import datetime
from src.severity import classify_risk

def generate_report(
    df,
    threat_counts,
    top_attackers,
    blocked_ips,
    risk_table
):

    report_path = "reports/security_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("=" * 60 + "\n")
        report.write("SOC SECURITY REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(
            f"Generated On: {datetime.now()}\n\n"
        )

        report.write(
            f"Total Logs Analyzed: {len(df)}\n\n"
        )
        highest_risk_ip = risk_table.index[0]
        highest_risk_score = risk_table.iloc[0]

        malicious_count = threat_counts.get("malicious", 0)
        suspicious_count = threat_counts.get("suspicious", 0)

        if malicious_count > 100000:
            overall_threat = "HIGH"
        elif malicious_count > 50000:
            overall_threat = "MEDIUM"
        else:
            overall_threat = "LOW"

        report.write("EXECUTIVE SUMMARY\n")
        report.write("-" * 30 + "\n")

        report.write(f"Total Events: {len(df)}\n")
        report.write(f"Malicious Events: {malicious_count}\n")
        report.write(f"Suspicious Events: {suspicious_count}\n")
        report.write(f"Highest Risk IP: {highest_risk_ip}\n")
        report.write(f"Highest Risk Score: {highest_risk_score}\n")
        report.write(f"Overall Threat Level: {overall_threat}\n\n")

        # Threat Summary
        report.write("THREAT SUMMARY\n")
        report.write("-" * 30 + "\n")

        for label, count in threat_counts.items():
            report.write(
                f"{label}: {count}\n"
            )

        report.write("\n")

        # Top Attacker IPs
        report.write("TOP ATTACKER IPS\n")
        report.write("-" * 30 + "\n")

        for ip, score in risk_table.items():

          severity = classify_risk(score)

          report.write(
        f"{ip}: {score} : {severity}\n"
    )

        report.write("\n")

        # Blocked IPs
        report.write("MOST BLOCKED IPS\n")
        report.write("-" * 30 + "\n")

        for ip, count in blocked_ips.items():
            report.write(
                f"{ip}: {count}\n"
            )

        report.write("\n")

        # Risk Scores
        report.write("TOP RISK IPS\n")
        report.write("-" * 30 + "\n")

        for ip, score in risk_table.items():
            report.write(
                f"{ip}: {score}\n"
            )

        report.write("\n")

        report.write("=" * 60 + "\n")
        report.write("END OF REPORT\n")
        report.write("=" * 60 + "\n")

    print(f"\nReport Saved: {report_path}")