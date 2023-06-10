import datetime
from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, lastServiceDate):
        self.lastServiceDate = lastServiceDate

    def needsService(self):
        date = datetime.date.today()

        if (date - self.lastServiceDate)/365 >= 2:
            return True
        else:
            return False