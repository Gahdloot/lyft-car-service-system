from battery import spindlerBattery
from battery import nubbinBattery
from engines import capuletEngine
from engines import sternmanEngine
from engines import willoughbyEngine
from lyft.car import Car

from datetime import datetime

class createCar:

    def create_calliope(self, last_service_date, current_millage, last_service_millage):
        battery = spindlerBattery(last_service_date)
        engine = capuletEngine(current_millage, last_service_millage)

        return Car(battery, engine).needs_sevice()

    def create_glissade(self, last_service_date, current_millage, last_service_millage):
        battery = spindlerBattery(last_service_date)
        engine = willoughbyEngine(current_millage, last_service_millage)

        return Car(battery, engine).needs_sevice()

    def create_palindrome(self, last_service_date, warning_light_on):
        battery = spindlerBattery(last_service_date)
        engine = sternmanEngine(warning_light_on)

        return Car(battery, engine).needs_sevice()

    def create_rorschach(self, last_service_date, current_millage, last_service_millage):
        battery = nubbinBattery(last_service_date)
        engine = willoughbyEngine(current_millage, last_service_millage)

        return Car(battery, engine).needs_sevice()


    def create_thovex(self, last_service_date, current_millage, last_service_millage):
        battery = nubbinBattery(last_service_date)
        engine = capuletEngine(current_millage, last_service_millage)

        return Car(battery, engine).needs_sevice()


print(createCar().create_calliope(datetime(2021, 3, 5, 23, 8, 15), 1000, 500))