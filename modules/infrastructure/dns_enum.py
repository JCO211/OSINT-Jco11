"""
OSINT Jco11 - DNS Enumeration Module
Enumeración DNS pasiva para dominios.
"""

import dns.resolver

from modules.base import OsintModule


class Module(OsintModule):
    name = "dns_enum"
    description = "Enumeración DNS pasiva (A, AAAA, MX, NS, TXT)"
    category = "infrastructure"
    target_types = ["domain"]
    noise_level = "LOW"
    timeout = 10

    async def run(self, target):
        domain = target["value"]
        resolver = dns.resolver.Resolver()

        records = {
            "A": [],
            "AAAA": [],
            "MX": [],
            "NS": [],
            "TXT": []
        }

        for record_type in records.keys():
            try:
                answers = resolver.resolve(domain, record_type)
                for rdata in answers:
                    records[record_type].append(str(rdata))
            except Exception:
                # DNS no encontrado o no existente → normal en OSINT
                continue

        return {
            "domain": domain,
            "records": records
        }
