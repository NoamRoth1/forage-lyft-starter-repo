from serviceable import Serviceable


class Car(Serviceable):

    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
