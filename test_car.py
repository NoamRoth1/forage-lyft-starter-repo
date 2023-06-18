import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.cf = CarFactory()
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_calliope(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_calliope(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def setUp(self):
        self.cf = CarFactory()
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_glissade(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_glissade(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.cf = CarFactory()
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_palindrome(today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_palindrome(self.today, last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_palindrome(self.today, last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def setUp(self):
        self.cf = CarFactory()
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        car = self.cf.create_rorschach(self.today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_rorschach(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def setUp(self):
        self.cf = CarFactory()
        self.today = datetime.today().date()

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_thovex(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        car = self.cf.create_thovex(self.today, last_service_date, current_mileage, last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
