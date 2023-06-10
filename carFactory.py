from battery.nubbinBattery import NubbinBattery
from battery.spindlerBaattery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def createCalliope(prevDistance, currDistance, lastServiceDate):
        engine = CapuletEngine(prevDistance, currDistance)
        battery = SpindlerBattery(lastServiceDate)
        car = Car(engine, battery)

        return car
    
    @staticmethod
    def createGlissade(currDistance, prevDistance, lastServiceDate):
        engine = WilloughbyEngine(currDistance, prevDistance)
        battery = SpindlerBattery(lastServiceDate)
        car = Car(engine, battery)

        return car
    
    @staticmethod
    def createPalindrome(warningLight, lastServiceDate):
        engine = SternmanEngine(warningLight)
        battery = SpindlerBattery(lastServiceDate)
        car = Car(engine, battery)

        return car
    
    @staticmethod
    def createRorschach(currDistance, prevDistance, lastServiceDate):
        engine = WilloughbyEngine(currDistance, prevDistance)
        battery = NubbinBattery(lastServiceDate)
        car = Car(engine, battery)

        return car
    
    @staticmethod
    def createThovex(prevDistance, currDistance, lastServiceDate):
        engine = CapuletEngine(prevDistance, currDistance)
        battery = NubbinBattery(lastServiceDate)
        car = Car(engine, battery)

        return car