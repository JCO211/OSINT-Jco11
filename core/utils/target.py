from urllib.parse import urlparse


def normalize_target(value: str, target_type: str):
    value = value.strip()

    if target_type in ("http", "https", "url"):
        parsed = urlparse(value)
        if parsed.hostname:
            return {
                "type": "domain",
                "value": parsed.hostname.lower()
            }

    if target_type == "domain":
        return {
            "type": "domain",
            "value": value.lower()
        }

    return {
        "type": target_type,
        "value": value
    }
