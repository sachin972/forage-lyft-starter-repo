from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warningLight):
        self.warningLight = warningLight

    def NeedsService(self):
        return self.warningLight
