from abc import ABC

from serviceable import Serviceable

from battery import Battery


from datetime import timedelta


class SpindlerBattery(Battery, Serviceable, ABC):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        time_difference = self.current_date - self.last_service_date
        two_years_ago = timedelta(days=365 * 2)

        if time_difference > two_years_ago:
            return True
        else:
            return False
