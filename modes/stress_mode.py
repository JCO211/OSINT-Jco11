import time
import requests


def stress_mode():
    print("\n[ STRESS / LOAD TEST MODE ]")
    print("⚠️ SOLO PARA SISTEMAS PROPIOS O AUTORIZADOS")

    if input("¿Confirmas autorización? (yes/no): ").lower() != "yes":
        print("Abortado.")
        return

    url = input("URL objetivo: ")
    count = int(input("Número de requests: "))
    delay = float(input("Delay entre requests (s): "))

    success = 0
    start = time.time()

    for _ in range(count):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code < 500:
                success += 1
        except Exception:
            pass
        time.sleep(delay)

    duration = round(time.time() - start, 2)

    print("\nResultado:")
    print(f"- Requests: {count}")
    print(f"- Exitosos: {success}")
    print(f"- Tiempo total: {duration}s")
