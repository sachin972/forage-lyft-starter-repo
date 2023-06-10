from engine.engine import Engine
from battery.battery import Battery

class Car(Engine, Battery):
    def __init__(self, Engine, Battery):
        # self.last_service_date = last_service_date
        self.Engine = Engine
        self.Battery = Battery

    def needs_service(self):
        return self.Engine.needsService() or self.Battery.needsService()
