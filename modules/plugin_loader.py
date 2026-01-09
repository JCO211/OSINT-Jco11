"""
OSINT Jco11 - Plugin Loader
Carga dinámica de módulos OSINT.
"""

import importlib
import pkgutil


def load_modules(package):
    modules = []

    for _, name, ispkg in pkgutil.iter_modules(package.__path__):
        if name == "base":
            continue

        module_path = f"{package.__name__}.{name}"
        module = importlib.import_module(module_path)

        if hasattr(module, "Module"):
            modules.append(module.Module())

    return modules
