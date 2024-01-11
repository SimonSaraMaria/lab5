from classes.identifier import Identifier


class Gericht(Identifier):         # Base class for the Cooked Dish and the Beverage classes

    def __init__(self, portionsgrosse, preis):
        super().__init__()
        self.portionsgrosse = portionsgrosse
        self.preis = preis

    def __str__(self):
        return f'Id: {self.id}, portionsgrosse: {self.portionsgrosse}, preis: {self.preis} '

    __repr__ = __str__