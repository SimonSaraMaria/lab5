class Identifier:       # Base class for Dish, Order and Customer
    id_count = 0

    def __init__(self):
        self.id = Identifier.id_count #id-ul ia valoarea contorului si il incrementam ca sa fie unic
        Identifier.id_count += 1

    def __lt__(self, other):
        return self.id < other.id