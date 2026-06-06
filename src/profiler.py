def profile_dataset(df):

    print("\n" + "=" * 50)
    print("DATASET PROFILE")
    print("=" * 50)

    print(f"\nTotal Rows    : {len(df)}")
    print(f"Total Columns : {len(df.columns)}")

    print("\nColumn Names:")

    for column in df.columns:
        print(f"- {column}")

    print("\nMissing Values:")

    print(df.isnull().sum())

    print("\nThreat Labels:")

    print(df["threat_label"].value_counts())

    print("\nActions:")

    print(df["action"].value_counts())

    print("\nProtocols:")

    print(df["protocol"].value_counts())

    print("\nLog Types:")

    print(df["log_type"].value_counts())