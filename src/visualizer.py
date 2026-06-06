import matplotlib.pyplot as plt


def threat_distribution(df):

    counts = df["threat_label"].value_counts()

    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar")

    plt.title("Threat Distribution")
    plt.xlabel("Threat Label")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig("graphs/threat_distribution.png")

    plt.close()

    print("Saved: threat_distribution.png")


def protocol_distribution(df):

    counts = df["protocol"].value_counts()

    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar")

    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig("graphs/protocol_distribution.png")

    plt.close()

    print("Saved: protocol_distribution.png")


def top_risk_ips_chart(risk_table):

    plt.figure(figsize=(10, 6))

    risk_table.sort_values().plot(kind="barh")

    plt.title("Top Risk IPs")
    plt.xlabel("Risk Score")

    plt.tight_layout()

    plt.savefig("graphs/top_risk_ips.png")

    plt.close()

    print("Saved: top_risk_ips.png")