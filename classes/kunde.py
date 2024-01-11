from classes.identifier import Identifier
from repository.kunde_repo import KundeRepository
class Kunde(Identifier):

            def __init__(self, name, adresse):
                super().__init__() #initializam metoda Identifier si ne asiguram ca cele 2 au aceeasi functionalitate
                self.name = name
                self.adresse = adresse
                kr = KundeRepository('customer.txt')
                try:  #ne asiguram ca id-ul nu se repeta prin verificarea fisierelor deja salvate
                    self.id = max(kr.read()).id + 1 #ia valoarea maxima din KundeRepository si incrementam cu 1 ca sa ne asiguram ca id-ul este unic
                except:
                    self.id = 0 #in caz de eroare setam valoarea id-ului la 0 si va fi atribuit urmatorului id disponibil cand se va salva

            def __str__(self):
                return f'{self.id} {self.name} - {self.adresse}\n'

            __repr__ = __str__