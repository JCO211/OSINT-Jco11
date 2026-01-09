# OSINT Jco11 – Security Toolkit

## 📌 Descripción

**OSINT Jco11 – Security Toolkit** es un framework modular desarrollado en **Python**, orientado exclusivamente a **OSINT pasivo**, **análisis defensivo**, **pruebas controladas de carga (stress testing legal)** y **detección de patrones anómalos** desde una perspectiva **Blue Team**.

El objetivo del proyecto es **educativo y profesional**, enfocado en el aprendizaje de:
- Reconocimiento pasivo
- Análisis de superficie de ataque
- Evaluación defensiva de tráfico
- Detección de comportamientos anómalos en logs

Este proyecto **NO está diseñado para ataques**, ni para la interrupción de servicios de terceros.

---

## ⚠️ Aviso legal (MUY IMPORTANTE)

Este software se proporciona **únicamente con fines educativos, defensivos y de análisis autorizado**.

### ❗ Condiciones de uso
- El usuario **es el único responsable** del uso que haga de esta herramienta.
- El software **solo debe utilizarse** en:
  - Sistemas propios
  - Sistemas con autorización explícita y verificable
- El autor **NO se responsabiliza** de:
  - Usos ilegales
  - Daños directos o indirectos
  - Interrupciones de servicio
  - Incumplimiento de leyes locales o internacionales

### 🚫 Prohibiciones explícitas
Este proyecto **NO debe utilizarse** para:
- Ataques de denegación de servicio (DDoS)
- Flooding
- Saturación de servicios de terceros
- Actividades maliciosas
- Acciones no autorizadas

El incumplimiento de estas condiciones **es responsabilidad exclusiva del usuario**.

---

## 🧠 Filosofía del proyecto

- 🔐 Ético por diseño
- 🧩 Modular y extensible
- 🟦 Orientado a Blue Team
- 📊 Resultados reales (no datos simulados falsos)
- 📚 Pensado para aprendizaje y portfolio profesional

---

## 📁 Estructura del proyecto

```text
OSINT-Jco11/
├── toolkit.py                 # Punto de entrada (menú principal)
├── cli/                       # CLI OSINT
├── core/                      # Motor del framework
├── modules/                   # Módulos OSINT
├── modes/                     # Modos de operación
│   ├── osint_mode.py
│   ├── stress_mode.py
│   └── defense_mode.py
├── defense/                   # Análisis defensivo / Blue Team
│   ├── log_analyzer.py
│   └── indicators.py
├── requirements.txt
└── README.md
