THRESHOLDS = {
    "requests_per_ip": 100,
    "error_rate": 0.3,
}


def risk_level(score: int):
    if score >= 3:
        return "ALTO"
    if score == 2:
        return "MEDIO"
    return "BAJO"
