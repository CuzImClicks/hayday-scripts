
class Crop:

    def __init__(self, name: str, time: float, sell: float):
        self.name = name
        self.time = time
        self.sell = sell

        self.sellPerMinute = sell / time

    def getSellPerMinute(self) -> float:
        return f"{self.name}: {self.sellPerMinute}"

    def toDict() -> dict:
        return {"name": self.name, "time": self.time, "sell": self.sell, "sellPerMinute": self.sellPerMinute}

    @classmethod
    def sort(array: list, value) -> dict:
        return sorted(array, lambda item: item[value])