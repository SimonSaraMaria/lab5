from ui.console import Console
from controller.kunde_controller import KundeController
from controller.gekochtergericht_controller import GekochterGerichtController
from controller.getrank_controller import GetrankController
from controller.bestellung_controller import BestellungController
from repository.kunde_repo import KundeRepository
from repository.bestellung_repo import BestellungRepo
from repository.gekochtergericht_repo import GekochterGerichtRepo
from repository.getrank_repo import GetrankRepo
from tests.tests import (test_adding_gericht, test_finding_kunde, test_edit_kunde_name, test_rechnung,
                         test_convert_and_save)
from classes.kunde import Kunde

app = Console(KundeController(KundeRepository('kunde.txt')),
              GekochterGerichtController(GekochterGerichtRepo('gekochtergericht.txt')),
              GetrankController(GetrankRepo('getrank.txt')), BestellungController(BestellungRepo("bestellung.txt")))


def tests():
    #test_adding_gericht()
    test_finding_kunde()
    test_edit_kunde_name()
    test_rechnung()
    test_convert_and_save()


tests()
# c = Customer('John', 'Str lui')
# cr = CustomerRepository('customer.txt')
# s = cr.convert_to_string([c, c, c])
# lists = cr.convert_from_string(s)
# print(lists)
# print(cr.read_file('customer_file.txt'))
# print(cr.read_file())
# cr.write_file('Customer: 1 Order: 16', 'customer_file.txt')


def main():
    app.run()


main()