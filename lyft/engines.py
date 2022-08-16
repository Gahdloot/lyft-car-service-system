class Engine:
    def needs_service(self, millage_requirement, millage_difference):
        return millage_difference > millage_requirement


class capuletEngine(Engine):
    millage_requirement = 30000

    def __init__(self,current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.millage_difference = self.current_mileage - self.last_service_mileage

        if self.last_service_mileage > self.current_mileage:
            raise ValueError('last service millage can\'t be higer than current millage')

    def needs_service(self):
        return Engine().needs_service(self.millage_requirement, self.millage_difference)



class willoughbyEngine:
    millage_requirement = 60000

    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.millage_difference = self.current_mileage - self.last_service_mileage

        if self.last_service_mileage > self.current_mileage:
            raise ValueError('last service millage can\'t be higer than current millage')

    def needs_service(self):
        return Engine().needs_service(self.millage_requirement, self.millage_difference)
