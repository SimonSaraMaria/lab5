from classes.gericht import Gericht
from repository.getrank_repo import GetrankRepo


class Getrank(Gericht):

    def __init__(self, portionsgrosse, preis, alkoholgehalt):
        super().__init__(portionsgrosse, preis)
        self.alkoholgehalt = alkoholgehalt
        gr = GetrankRepo('getrank.txt')
        try:
            self.id = max(gr.read()).id + 1
        except:
            self.id = 0

    def __str__(self):
        return super().__str__() + f'Alkoholgehalt: {self.alkoholgehalt}\n'

    __repr__ = __str__
