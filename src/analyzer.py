def threat_summary(df):

    print("\n" + "=" * 50)
    print("THREAT SUMMARY")
    print("=" * 50)

    threat_counts = df["threat_label"].value_counts()

    print(threat_counts)

    return threat_counts


def top_attacker_ips(df, top_n=10):

    print("\n" + "=" * 50)
    print("TOP SOURCE IPS")
    print("=" * 50)

    attackers = (
        df[df["threat_label"] != "benign"]
        ["source_ip"]
        .value_counts()
        .head(top_n)
    )

    print(attackers)

    return attackers


def blocked_ips(df, top_n=10):

    print("\n" + "=" * 50)
    print("MOST BLOCKED IPS")
    print("=" * 50)

    blocked = (
        df[df["action"] == "blocked"]
        ["source_ip"]
        .value_counts()
        .head(top_n)
    )

    print(blocked)

    return blocked


def detect_security_tools(df):

    print("\n" + "=" * 50)
    print("SECURITY TOOL DETECTION")
    print("=" * 50)

    tools = [
        "Nmap",
        "SQLMap",
        "curl"
    ]

    for tool in tools:

        matches = df[
            df["user_agent"]
            .str.contains(tool, case=False, na=False)
        ]

        print(f"{tool}: {len(matches)} events")