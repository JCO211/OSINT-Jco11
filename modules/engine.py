"""
OSINT Jco11 - Core Engine
Responsable de ejecutar módulos OSINT de forma controlada.
"""

from typing import List, Dict, Any


class OsintEngine:
    def __init__(self):
        self.modules = []

    def register_module(self, module) -> None:
        """
        Registra un módulo OSINT en el engine.
        """
        self.modules.append(module)

    async def run(self, target: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Ejecuta todos los módulos compatibles con el target.
        """
        results = []

        for module in self.modules:
            if module.supports(target["type"]):
                output = await module.execute(target)
                results.append(output)

        return results
