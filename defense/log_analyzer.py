from collections import defaultdict
from defense.indicators import THRESHOLDS, risk_level


def analyze_logs(log_path: str):
    ip_count = defaultdict(int)
    errors = 0
    total = 0

    with open(log_path, "r", errors="ignore") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 9:
                continue

            ip = parts[0]
            status = parts[8]

            ip_count[ip] += 1
            total += 1

            if status.startswith("4") or status.startswith("5"):
                errors += 1

    score = 0

    if max(ip_count.values(), default=0) > THRESHOLDS["requests_per_ip"]:
        score += 1

    if total > 0 and (errors / total) > THRESHOLDS["error_rate"]:
        score += 1

    return {
        "total_requests": total,
        "unique_ips": len(ip_count),
        "max_requests_ip": max(ip_count.values(), default=0),
        "error_rate": round(errors / total, 2) if total else 0,
        "risk": risk_level(score),
    }
