import unittest
from datetime import datetime

from lyft.battery import nubbinBattery
from lyft.battery import spindlerBattery
from lyft.engines import capuletEngine
from lyft.engines import sternmanEngine
from lyft.engines import willoughbyEngine
from lyft.create_car import createCar


class TestBattery(unittest.TestCase):
    def test_spindler_battery_with_dates_longer_than_requirement(self):
        later_date_1 = datetime(2012, 3, 5, 23, 8, 15)
        later_date_2 = datetime(2013, 3, 5, 23, 8, 15)
        later_date_3 = datetime(2015, 3, 5, 23, 8, 15)
        later_date_4 = datetime(2016, 3, 5, 23, 8, 15)
        later_date_5 = datetime(2019, 3, 5, 23, 8, 15)
        battery = spindlerBattery(later_date_1)
        battery_2 = spindlerBattery(later_date_2)
        battery_3 = spindlerBattery(later_date_3)
        battery_4 = spindlerBattery(later_date_4)
        battery_5 = spindlerBattery(later_date_5)

        self.assertTrue(battery)
        self.assertTrue(battery_2)
        self.assertTrue(battery_3)
        self.assertTrue(battery_4)
        self.assertTrue(battery_5)

    def test_spindler_battery_with_recent_dates(self):
        later_date_1 = datetime(2021, 3, 5, 23, 8, 15)
        later_date_2 = datetime(2021, 4, 5, 23, 8, 15)
        later_date_3 = datetime(2022, 8, 5, 23, 8, 15)
        later_date_4 = datetime(2022, 9, 5, 23, 8, 15)
        later_date_5 = datetime(2022, 1, 5, 23, 8, 15)
        battery = spindlerBattery(later_date_1)
        battery_2 = spindlerBattery(later_date_2)
        battery_3 = spindlerBattery(later_date_3)
        battery_4 = spindlerBattery(later_date_4)
        battery_5 = spindlerBattery(later_date_5)

        self.assertFalse(battery)
        self.assertFalse(battery_2)
        self.assertFalse(battery_3)
        self.assertFalse(battery_4)
        self.assertFalse(battery_5)

    def test_nubbin_battery_with_dates_longer_than_requirement(self):
        later_date_1 = datetime(2012, 3, 5, 23, 8, 15)
        later_date_2 = datetime(2013, 3, 5, 23, 8, 15)
        later_date_3 = datetime(2015, 3, 5, 23, 8, 15)
        later_date_4 = datetime(2016, 3, 5, 23, 8, 15)
        later_date_5 = datetime(2019, 3, 5, 23, 8, 15)
        battery = nubbinBattery(later_date_1)
        battery_2 = nubbinBattery(later_date_2)
        battery_3 = nubbinBattery(later_date_3)
        battery_4 = nubbinBattery(later_date_4)
        battery_5 = nubbinBattery(later_date_5)

        self.assertTrue(battery)
        self.assertTrue(battery_2)
        self.assertTrue(battery_3)
        self.assertTrue(battery_4)
        self.assertTrue(battery_5)

    def test_nubbin_battery_with_recent_dates(self):
        later_date_1 = datetime(2021, 3, 5, 23, 8, 15)
        later_date_2 = datetime(2021, 4, 5, 23, 8, 15)
        later_date_3 = datetime(2022, 8, 5, 23, 8, 15)
        later_date_4 = datetime(2022, 9, 5, 23, 8, 15)
        later_date_5 = datetime(2022, 1, 5, 23, 8, 15)
        battery = nubbinBattery(later_date_1)
        battery_2 = nubbinBattery(later_date_2)
        battery_3 = nubbinBattery(later_date_3)
        battery_4 = nubbinBattery(later_date_4)
        battery_5 = nubbinBattery(later_date_5)

        self.assertFalse(battery)
        self.assertFalse(battery_2)
        self.assertFalse(battery_3)
        self.assertFalse(battery_4)
        self.assertFalse(battery_5)




class TestEngine(unittest.TestCase):
    def test_capulet_Engine(self):
        current_millage_1 = 100000
        last_service_millage_1 = 69000
        last_service_millage_2 = 71000
        check_1 = capuletEngine(current_millage_1, last_service_millage_1).needs_service()
        check_2 = capuletEngine(current_millage_1, last_service_millage_2).needs_service()
        self.assertFalse(check_1)
        self.assertTrue(check_2)

    def test_willoughby_Engine(self):
        current_millage_1 = 100000
        last_service_millage_1 = 39000
        last_service_millage_2 = 41000
        check_1 = willoughbyEngine(current_millage_1, last_service_millage_1).needs_service()
        check_2 = willoughbyEngine(current_millage_1, last_service_millage_2).needs_service()
        self.assertFalse(check_1)
        self.assertTrue(check_2)

    def test_sternman_Engine(self):
        self.assertTrue(sternmanEngine(True).needs_service())
        self.assertFalse(sternmanEngine(False).needs_service())

class TestCalliope(unittest.TestCase):
    def test_car_not_should_be_serviced(self):
        last_service_date = datetime(2021, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0


        car = createCar().create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car)

    def test_car_should_be_serviced(self):
        last_service_date = datetime(2002, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0

        car = createCar().create_calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car)

class TestGlissade(unittest.TestCase):
    def test_car_not_should_be_serviced(self):
        last_service_date = datetime(2021, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0


        car = createCar().create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car)

    def test_car_should_be_serviced(self):
        last_service_date = datetime(2002, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0

        car = createCar().create_glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car)

class TestPalindrome(unittest.TestCase):
    def test_car_not_should_be_serviced(self):
        last_service_date = datetime(2021, 3, 5, 23, 8, 15)
        warning_indicator = False


        car = createCar().create_palindrome(last_service_date, warning_indicator)
        self.assertFalse(car)

    def test_car_should_be_serviced(self):
        def test_car_not_should_be_serviced(self):
            last_service_date = datetime(2021, 3, 5, 23, 8, 15)
            warning_indicator = True

            car = createCar().create_palindrome(last_service_date, warning_indicator)
            self.assertTrue(car)


class TestRorschach(unittest.TestCase):
    def test_car_not_should_be_serviced(self):
        last_service_date = datetime(2021, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0


        car = createCar().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car)

    def test_car_should_be_serviced(self):
        last_service_date = datetime(2002, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0

        car = createCar().create_rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car)


class TestThovex(unittest.TestCase):
    def test_car_not_should_be_serviced(self):
        last_service_date = datetime(2021, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0


        car = createCar().create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car)

    def test_car_should_be_serviced(self):
        last_service_date = datetime(2002, 3, 5, 23, 8, 15)
        current_mileage = 10
        last_service_mileage = 0

        car = createCar().create_thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car)





if __name__ == '__main__':
    unittest.main()