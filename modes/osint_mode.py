import os


def osint_mode():
    print("\n[ OSINT MODE ]")
    target = input("Target: ")
    ttype = input("Tipo (domain, url, ip): ")

    os.system(
        f"python -m cli.main scan run --target \"{target}\" --type {ttype}"
    )
