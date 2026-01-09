import importlib
import pkgutil

def load_modules(package):
    modules = []
    for _, name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package.__name__}.{name}")
        if hasattr(module, "Module"):
            modules.append(module.Module())
    return modules
