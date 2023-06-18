from car import Car

from battery import Battery

from engine import Engine


class CarFactory(Car, Battery, Engine):
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(current_date, last_service_date, warning_light_on)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)
