from typing import List
class CarriganTires:
    def __init__(self, array:List):
        self.array = array

    def needs_servicing(self):
        for i in self.array:
            if i >= 0.9:
                break
        return True


class OctoprimeTires:
    def __init__(self, array: List):
        self.array = array

    def needs_servicing(self):
        return sum(self.array) >= 3


