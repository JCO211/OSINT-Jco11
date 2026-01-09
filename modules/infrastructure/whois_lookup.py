import whois
from datetime import datetime
from modules.base import OsintModule


class Module(OsintModule):
    name = "whois_lookup"
    category = "infrastructure"
    target_types = ["domain"]

    async def run(self, target):
        domain = target["value"]

        try:
            w = whois.whois(domain)
        except Exception as e:
            # WHOIS no disponible es información válida
            return {
                "domain": domain,
                "whois_available": False,
                "reason": str(e),
            }

        return {
            "domain": domain,
            "whois_available": True,
            "registrar": _one(w.registrar),
            "creation_date": _date(w.creation_date),
            "expiration_date": _date(w.expiration_date),
            "name_servers": _list(w.name_servers),
            "org": _one(w.org),
            "country": _one(w.country),
        }


def _one(v):
    if isinstance(v, list):
        return v[0]
    return v


def _list(v):
    if not v:
        return []
    return list(set(v if isinstance(v, list) else [v]))


def _date(v):
    if isinstance(v, list):
        v = v[0]
    if isinstance(v, datetime):
        return v.isoformat()
    return str(v) if v else None
