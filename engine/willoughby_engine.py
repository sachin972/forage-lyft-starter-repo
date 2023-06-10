from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, currentDistance, previousDistance):
        self.currDistance = currentDistance
        self.prevDistance = previousDistance

    def needsService(self):
        return self.currDistance - self.prevDistance > 60000
