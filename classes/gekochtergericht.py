from classes.gericht import Gericht
from repository.gekochtergericht_repo import GekochterGerichtRepo


class GekochterGericht(Gericht):

    def __init__(self, portionsgrosse, preis , voraussichtlicheLd):
        super().__init__(portionsgrosse, preis)
        self.voraussichtlicheLd = voraussichtlicheLd
        ggr = GekochterGerichtRepo('gekochtergericht.txt')
        try:
            self.id = max(ggr.read()).id + 1
        except:
            self.id = 0

    def __str__(self):
        return super().__str__() + f"Voraussichtliche Lieferdatum: {self.voraussichtlicheLd}\n"

    __repr__ = __str__