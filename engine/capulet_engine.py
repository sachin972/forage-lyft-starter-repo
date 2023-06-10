from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, prevDistance, currDistance):
        self.currentDitance = currDistance
        self.previousDitance = prevDistance

    def needsService(self):
        return self.currentDistance - self.previousDistance > 30000
