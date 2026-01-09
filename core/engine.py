import time


class OsintEngine:
    def __init__(self):
        self.modules = []

    def register_module(self, module):
        self.modules.append(module)

    async def run(self, target: dict):
        results = []

        for module in self.modules:
            if target["type"] not in module.target_types:
                continue

            start = time.time()

            result = await module.execute(target)

            # Blindaje final
            result.setdefault("module", module.name)
            result.setdefault("category", module.category)
            result["execution_time"] = round(time.time() - start, 2)

            results.append(result)

        return results
