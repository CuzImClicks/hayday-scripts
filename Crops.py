
class Crop:

    def __init__(name: str, time: float, sell: float):
        self.name = name
        self.time = time
        self.sell = sell

        self.sellPerMinute = sell / time

    def getSellPerMinute() -> float:
        return self.sellPerMinute

diff --git a/main.py b/main.py
