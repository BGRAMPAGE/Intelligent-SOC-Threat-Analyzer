import pandas as pd


def calculate_risk_scores(df):

    threat_weights = {
        "benign": 1,
        "suspicious": 5,
        "malicious": 10
    }

    temp = df.copy()

    temp["risk_score"] = temp["threat_label"].map(
        threat_weights
    )

    risk_table = (
        temp.groupby("source_ip")["risk_score"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n" + "=" * 50)
    print("TOP RISK IPS")
    print("=" * 50)

    print(risk_table)

    return risk_table