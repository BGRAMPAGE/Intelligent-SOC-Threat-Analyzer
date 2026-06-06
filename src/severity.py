def classify_risk(score):

    if score >= 30000:
        return "CRITICAL"

    elif score >= 20000:
        return "HIGH"

    elif score >= 10000:
        return "MEDIUM"

    else:
        return "LOW"