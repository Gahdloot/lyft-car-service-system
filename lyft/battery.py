class Battery:
    def needs_service(self, requirements, service_difference):
        return service_difference > requirements



class spindlerBattery(Battery):
    requirements = 2

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

        self.service_difference = self.current_date - self.last_service_date

    def needs_service(self):
        Battery().needs_service(self.requirements, self.service_difference)

class nubbinBattery(Battery):
    requirements = 4

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

        self.service_difference = current_date - last_service_date

    def needs_service(self):
        Battery().needs_service(self.requirements, self.service_difference)
