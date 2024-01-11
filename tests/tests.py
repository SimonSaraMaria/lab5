from classes.gekochtergericht import GekochterGericht
from classes.getrank import Getrank
from repository.gekochtergericht_repo import GekochterGerichtRepo
from repository.getrank_repo import GetrankRepo
from repository.kunde_repo import KundeRepository
from controller.kunde_controller import KundeController
from classes.bestellung import Bestellung
from repository.bestellung_repo import BestellungRepo


def test_adding_gericht():
    """
    Test adding Cooked Dishes and Beverages
    :return:
    """
    gekochtergericht_repo = GekochterGerichtRepo('gekochtergericht.txt')
    getrank_repo = GetrankRepo('getrank.txt')
    gekochtergericht_repo.add_item(GekochterGericht('230g', 123, 120))
    beverage_repo.add_item(Getrank('260ml', 12, 12))
    assert gekochtergericht_repo.load()[len(gekochtergericht_repo.load()) - 1].portionsgrosse == '230g'
    assert gekochtergericht_repo.load()[len(gekochtergericht_repo.load()) - 1].preis == 123
    assert gekochtergericht_repo.load()[len(gekochtergericht_repo.load()) - 1].voraussichtlicheLd == 120
    assert getrank_repo.load()[len(getrank_repo.load()) - 1].portionsgrosse == '260ml'
    assert getrank_repo.load()[len(getrank_repo.load()) - 1].preis == 12
    assert getrank_repo.load()[len(getrank_repo.load()) - 1].alkoholgehalt == 12


def test_finding_kunde():
    """
    Test the finding a customer by partial name or partial address
    :return:
    """
    kunde_controller = KundeController(KundeRepository('kunde.txt'))
    for term in kunde_controller.find_items('Plop'):
        assert 'Plop' in term.adresse
        assert 'Plop' not in term.name

    for term in kunde_controller.find_items('John'):
        assert 'John' in term.name
        assert 'John' not in term.adresse


def test_edit_kunde_name():
    """
    Test the editing the customer name
    :return:
    """
    kunde_controller = KundeController(KundeRepository('kunde.txt'))
    kunde_controller.edit_kunde(3, "Changed", "Street")
    assert kunde_controller.find_by_id(3).name == 'Changed'


def test_convert_and_save():
    """
    Creates an order and converts it into a string that represents a byte of an order.
    That string is then saved onto a file and then retrieved from the file
    The string is then converted into a byte again and used to retrieve the order that was originally saved
    :return:
    """
    order_repo = OrderRepo('order_file.txt')
    obj_list_string = order_repo.convert_to_string([Order(3, [1, 1, 0], [2, 3, 2]), Order(4, [3, 2, 1], [])])
    for obj in obj_list_string:
        order_repo.write_file(str(obj), 'order_file.txt')
    obj_list = order_repo.read_file('order_file.txt')
    obj_list = order_repo.convert_from_string(obj_list)
    for obj in obj_list:
        assert obj.kunde_id == 4
        assert obj.gericht_ids == [3, 2, 1]
        assert obj.getrank_ids == []


def test_rechnung():
    neue_bestellung = Order(9, [0, 1, 1], [1, 1])
    rechnung = neue_bestellung.show_rechnung()
    assert rechnung == """The 0. item                  24 Ron
The 1. item                  100 Ron
The 2. item                  100 Ron
The 3. item                  15 Ron
The 4. item                  15 Ron
The total of the order is    254.0 Ron"""