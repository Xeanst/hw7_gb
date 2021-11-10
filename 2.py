from abc import abstractmethod

class Clothes:
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __str__(self):
        return str(self.parameter)

class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return self.parameter / 6.5 + 0.5

class Costume(Clothes):

    @property
    def fabric_consumption(self):
        return self.parameter * 2 + 0.3

coat = Coat(57)
costume = Costume(7)
print(coat.fabric_consumption)
print(costume.fabric_consumption)