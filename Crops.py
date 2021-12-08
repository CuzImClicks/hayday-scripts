
class Crop:

    def __init__(self, name: str, time: float, sell: float):
        self.name = name
        self.time = time
        self.sell = sell

        self.sellPerMinute = sell / time

    def getSellPerMinute(self) -> float:
        return f"{self.name}: {self.sellPerMinute}"
