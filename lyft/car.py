from battery import spindlerBattery
from battery import nubbinBattery
from engines import capuletEngine
from engines import sternmanEngine
from engines import willoughbyEngine
from tires import OctoprimeTires, CarriganTires


class Car:
    def __init__(self, battery, engine, tires):
        self.battery = battery
        self.engine = engine
        self.tires = tires


    def needs_sevice(self):
        components = [self.battery.needs_service(), self.engine.needs_service(), self.tires.needs_service()]
        result = any(component for component in components)
        return result


