from classes.identifier import Identifier
from repository.gekochtergericht_repo import GekochterGerichtRepo
from repository.getrank_repo import GetrankRepo
from repository.bestellung_repo import BestellungRepo
import functools


class Bestellung(Identifier):

    def __init__(self, kunde_id: int, gericht_ids: list, getrank_ids: list):
        super().__init__()
        self.kunde_id = kunde_id
        self.gericht_ids = gericht_ids
        self.getrank_ids = getrank_ids
        self.preis = 0
        self.calculate_preis()
        bestellung_repo = BestellungRepo('bestellung.txt')
        try:
            self.id = max(bestellung_repo.read()).id + 1
        except:
            self.id = 0

    def __gerichte_liste(self):
        """
        A private methode for creating a list of all the prices of the cooked dishes and beverages that are in an order
        :return: A list of float numbers representing the prices
        """
        gekochtergericht_repo = GekochterGerichtRepo('gekochtergericht.txt')
        getrank_repo = GetrankRepo('getrank.txt')
        gerichte = ([dish.preis for gericht_id in self.gericht_ids for gericht in gekochtergericht_repo.load() if gericht.id == gericht_id] +
                  [getrank.price for getrank_id in self.getrank_ids for getrank in getrank_repo.load()
                   if getrank_id == getrank.id])
        return gerichte

    def calculate_preis(self):
        """
        A methode for calculating the price of the order based on the dish and beverage ids
        :return:
        """
        gerichte = self.__gerichte_liste()
        try:
            self.preis = functools.reduce(lambda a, b: float(a) + float(b), gerichte)
        except TypeError:
            self.preis = 0

    def __create_rechnung(self):
        """
        A private methode for creating how the receipt should look like
        :return: A string representing the receipt
        """
        gerichte = self.__gerichte_liste()
        indexes = [x for x in range(len(gerichte))]
        rechnung = map(lambda a, b: f"The {b}. item                  {a} Ron", gerichte, indexes)
        rechnung = '\n'.join(list(rechnung))
        return rechnung + f"\nDie Summe der Bestellung ist    {self.preis} Ron"

    def show_rechnung(self):
        return self.__create_rechnung()

    def __str__(self):
        return (f"Bestellung {self.id}: Kunde Id: {self.kunde_id}, Gericht Ids: {self.gericht_ids} , Getrank Ids:"
                f" {self.getrank_ids}, Preis: {self.preis}\n")

    __repr__ = __str__