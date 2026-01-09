from defense.log_analyzer import analyze_logs


def defense_mode():
    print("\n[ DEFENSE MODE - DDoS Detection ]")
    log = input("Ruta del log (apache/nginx): ")

    try:
        result = analyze_logs(log)
    except FileNotFoundError:
        print("❌ Log no encontrado")
        return

    print("\nResultado del análisis:")
    for k, v in result.items():
        print(f"- {k}: {v}")
