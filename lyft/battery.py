class Battery:
    def needs_service(self, requirements, service_difference):
        return service_difference > requirements


from datetime import datetime


class spindlerBattery(Battery):
    requirements = 2

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

        duration_in_seconds =  (datetime.now() - self.last_service_date).total_seconds()
        self.years = divmod(duration_in_seconds, 31536000)[0]


    def needs_service(self):
        return Battery().needs_service(self.requirements, self.years)

class nubbinBattery(Battery):
    requirements = 4

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

        duration_in_seconds = (datetime.now() - self.last_service_date).total_seconds()
        self.years = divmod(duration_in_seconds, 31536000)[0]

    def needs_service(self):
        return Battery().needs_service(self.requirements, self.years)





