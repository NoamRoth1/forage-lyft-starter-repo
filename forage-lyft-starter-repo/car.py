from abc import ABC

from serviceable import Serviceable


class Car(Serviceable, ABC):

    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self) -> bool:
        pass
