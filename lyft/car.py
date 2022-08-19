from battery import spindlerBattery
from battery import nubbinBattery
from engines import capuletEngine
from engines import sternmanEngine
from engines import willoughbyEngine
class Car:
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_sevice(self):
        components = [self.battery.needs_service(), self.engine.needs_service()]
        result = any(component for component in components)
        return result


