class OsintModule:
    name = "base"
    description = ""
    category = "generic"
    target_types = []
    noise_level = "LOW"

    async def execute(self, target):
        try:
            data = await self.run(target)

            return {
                "module": self.name,
                "category": self.category,
                "status": "success",
                "data": data,
            }

        except Exception as e:
            return {
                "module": self.name,
                "category": self.category,
                "status": "error",
                "error": str(e),
            }

    async def run(self, target):
        raise NotImplementedError
