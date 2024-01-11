from classes.getrank import Getrank
from classes.bestellung import Bestellung
from classes.kunde import Kunde
from classes.gekochtergericht import GekochterGericht


def menu():
    return """
            1 - Neue Bestellung hinzufügen
            2 - Alle Bestellungen anzeigen
            3 - Bestehende Bestellung bearbeiten
            4 - Bestellung löschen
            5 - Kunden suchen
            6 - Ein Gericht hinzufügen
            7 - CRUD Kunde
            8 - CRUD Gericht
            9 - Zeige die Rechnung für die Bestellung
            0 - Exit
            """


def crud():
    """
    Menu for the CRUD Operations
    :return: the menu in string format
    """
    return """
            1 - Add
            2 - View
            3 - Edit
            4 - Delete
           """


def neue_kunde():
    """
    Creates a new customer
    :return: A customer with attributes read from the user
    """
    name = input("Name: ")
    adresse = input("Adresse: ")
    neue_kund = Kunde(name, adresse)
    return neue_kund()


def neue_gericht():
    """
    Creates a new cooked dish or a new Beverage
    :return: A cooked dish or Beverage with attributes read from the user
    """
    print(" Wählen Sie, welche Art von Gericht hinzufügen: \n 1 - Gekochter Gericht \n 2 - Getrank")
    gericht_typ = int(input("Wählen Sie, welche Art von Gericht hinzufügen: "))
    portionsgrosse = input("Geben Sie die Portionsgröße ein: ")
    preis = int(input("Geben Sie den Preis ein: "))
    if gericht_typ == 1:
        voraussichtlicheLd = int(input("Geben Sie die benötigte Zeit ein: "))
        return GekochterGericht(portionsgrosse, preis, voraussichtlicheLd)
    if gericht_typ == 2:
        alkoholgehalt = int(input("Geben Sie das Alkoholgehalt ein: "))
        return Getrank(portionsgrosse, preis, alkoholgehalt)


class Console:
    def __init__(self, kunde_kontroller, gekochtergericht_controller, getrank_controller,
                 bestellung_controller):
        self.kunde_kontroller = kunde_kontroller
        self.gekochtergericht_controller = gekochtergericht_controller
        self.getrank_controller = getrank_controller
        self.bestellung_controller = bestellung_controller

    def delete_bestellung(self):
        """
        prints all the orders then deletes the order with the ID input by the user
        :return:
        """
        while True:
            print(self.view_bestellungen())
            bestellung_id = int(input("Wählen Sie, welche Reihenfolge nach ID gelöscht werden soll: "))
            if self.bestellung_controller.validate_id(bestellung_id):
                break
            else:
                print("Ungültiger Wert")
        self.bestellung_controller.delete_item(bestellung_id)

    def crud_kunde(self, opt):
        """
        Calls the methods for the crud operations
        :param opt: the operation that will be done
        :return:
        """
        if opt == 1:
            self.add_kunde()
        elif opt == 2:
            self.view_kunden()
        elif opt == 3:
            self.edit_kunde()
        elif opt == 4:
            self.delete_kunde()

    def add_kunde(self):
        """
        Adds a new customer
        :return:
        """
        kunde = neue_kunde()
        self.kunde_controller.add_item(kunde)

    def view_kunden(self):
        """
        Prints a list of all customers
        :return:
        """
        print(self.kunde_controller.view_items())

    def edit_kunde(self):
        """
        Edits the customer by the ID the user has chosen
        :return:
        """
        self.find_kunde()
        while True:
            kunde_id = int(input("Wählen Sie den Kunden nach ID: "))
            if self.kunde_controller.validate_id(kunde_id):
                break
            else:
                print("Ungültiger Wert")
        kunde = self.kunde_controller.find_by_id(kunde_id)
        while True:
            print("Was möchten Sie bearbeiten?\n1-Name\n2-Adresse\n0-Exit")
            edit_option = int(input("Wählen Sie die Option: "))
            if edit_option == 1:
                name = input("Name: ")
                kunde.name = name
            elif edit_option == 2:
                adresse = input("Adresse: ")
                kunde.adresse = adresse
            elif edit_option == 0:
                break
        self.kunde_controller.edit_kunde(kunde.id, customer.name, kunde.adresse)

    def delete_kunde(self):
        """
        Deletes the Customer and checks for orders with that customer to delete
        :return:
        """
        self.find_kunde()
        while True:
            kunde_id = int(input("Wählen Sie den Kunden nach ID: "))
            if self.kunde_controller.validate_id(kunde_id):
                break
            else:
                print("Ungültiger Wert")
        self.kunde_controller.delete_item(kunde_id)
        self.bestellung_controller.validate_kunde_id(kunde_id)

    def crud_dishes(self, opt):
        """
        Crud of the Operations for the Dishes
        :param opt:
        :return:
        """
        if opt == 1:
            self.add_gericht()
        elif opt == 2:
            self.view_gerichte()
        elif opt == 3:
            self.edit_gerichte()
            self.bestellung_controller.recalculate_preis()
        elif opt == 4:
            self.delete_gerichte()
            self.bestellung_controller.recalculate_preis()

    def add_gericht(self):
        """
        Adds a Cooked Dish or a Beverage
        :return:
        """
        gericht = neue_gericht()
        if isinstance(gericht, GekochterGericht):
            self.gekochtergericht_controller.add_item(gericht)
        elif isinstance(gericht, Getrank):
            self.getrank_controller.add_item(gericht)

    def view_gerichte(self):
        """
        Prints both Cooked Dishes and Beverages
        :return:
        """
        print("Gekochte Gerichte: \n")
        print(self.gekochtergericht_controller.view_items())
        print("Getranke: \n")
        print(self.getrank_controller.view_items())

    def edit_gerichte(self):
        """
        Edits Cooked Dishes and Beverages
        :return:
        """
        print("Was möchten Sie bearbeiten: \n1 - Gekochte Gerichte\n2 - Getranke")
        gericht_option = int(input("Wählen Sie die Option: "))
        if gericht_option == 1:
            self.edit_gekochtergericht()
        elif gericht_option == 2:
            self.edit_getrank()

    def edit_gekochtergericht(self):
        """
        Edits the cooked Dishes
        :return:
        """
        while True:
            print(self.gekochtergericht_controller.view_items())
            gekochtergericht_id = input("Wählen Sie das Gericht Id: ")
            if self.gekochtergericht_controller.validate_id(gekochtergericht_id):
                break
            else:
                print("Ungültiger Wert")
        gekochtergericht = self.gekochtergericht_controller.find_by_id(gekochtergericht_id)
        while True:
            print("Was möchten Sie bearbeiten?\n1 - Portionsgröße\n2 - Preis\n3 - Gebrauchte Zeit\n0 - Stop")
            edit_option = int(input("Wählen Sie die Option: "))
            if edit_option == 1:
                portionsgrosse = input("Portionsgröße: ")
                gekochtergericht.portionsgrosse = portionsgrosse
            elif edit_option == 2:
                preis = input("Preis: ")
                gekochtergericht.preis = preis
            elif edit_option == 3:
                voraussichtlicheLd = input("Gebrauchte Zeit: ")
                gekochtergericht.voraussichtlicheLd = voraussichtlicheLd
            elif edit_option == 0:
                break
        self.gekochtergericht_controller.edit_gekochtergericht(gekochtergericht.id, gekochtergericht.portionsgrosse,
                                                     gekochtergericht.preis, gekochtergericht.voraussichtlicheLd)

    def edit_getrank(self):
        """
        Edits the Beverages
        :return:
        """
        while True:
            print(self.getrank_controller.view_items())
            getrank_id = input("Wählen Sie das Getränk Id: ")
            if self.getrank_controller.validate_id(getrank_id):
                break
            else:
                print("Ungültiger Wert")
        getrank = self.getrank_controller.find_by_id(getrank_id)
        while True:
            print("Was möchten Sie bearbeiten?\n1 - Portionsgröße\n2 - Preis\n3 - Alkoholgehalt\n0 - Stop")
            edit_option = int(input("Wählen Sie die Option: "))
            if edit_option == 1:
                portionsgrosse = input("Portionsgröße: ")
                getrank.portionsgrosse = portionsgrosse
            elif edit_option == 2:
                preis = input("Preis: ")
                getrank.preis = preis
            elif edit_option == 3:
                alkoholgehalt = input("Alkoholgehalt: ")
                getrank.alkoholgehalt = alkoholgehalt
            elif edit_option == 0:
                break
        self.getrank_controller.edit_getrank(getrank.id, getrank.portionsgrosse,
                                               getrank.preis, getrank.alkoholgehalt)

    def delete_gerichte(self):
        """
        Deletes eiter a cooked Dish or a Beverage
        :return:
        """
        print("Gekochte Gerichte: \n")
        print(self.gekochtergericht_controller.view_items())
        print("Getranke: \n")
        print(self.getrank_controller.view_items())
        print("Was möchten Sie löschen?\n1 - Gekochter Gericht\n2 - Getrank")
        delete_option = int(input("Wählen Sie die Option: "))
        if delete_option == 1:
            while True:
                gericht_id = int(input("Wählen Sie das Gericht nach Id: "))
                if self.gekochtergericht_controller.validate_id(gericht_id):
                    break
                else:
                    print("Ungültiger Wert")
            self.gekochtergericht_controller.delete_item(gericht_id)
            self.bestellung_controller.validate_gericht_id(gericht_id, delete_option)
        elif delete_option == 2:
            while True:
                gericht_id = int(input("Wählen Sie das Gericht nach Id: "))
                if self.getrank_controller.validate_id(gericht_id):
                    break
                else:
                    print("Ungültiger Wert")
            self.getrank_controller.delete_item(gericht_id)
            self.bestellung_controller.validate_gericht_id(gericht_id, delete_option)

    def crud_operations(self, class_option):
        """
        Calls either the menu for the crud operations for the customer or the dishes
        :param class_option:
        :return:
        """
        print(crud())
        opt = int(input("Choose which: "))
        if class_option == 7:
            self.crud_kunde(opt)
        if class_option == 8:
            self.crud_gerichte(opt)

    def edit_bestellung(self):
        while True:
            print(self.view_bestellungen())
            bestellung_id = int(input("Wählen Sie, welche Bestellung nach ID bearbeitet werden soll: "))
            if self.bestellung_controller.validate_id(order_id):
                break
            else:
                print("Ungültiger Wert")
        bestellung = self.bestellung_controller.find_by_id(bestellung_id)
        while True:
            print("1 - Bearbeiten Sie gekochte Gerichte\n2 - Bearbeiten Sie Getränke \n3 - Bearbeiten Sie Kunden\n0 - Stop")
            option = int(input("Bitte wählen: "))
            if option == 1:
                gericht_ids = self.gericht_ids_to_list()
                bestellung.gericht_ids = gericht_ids
            if option == 2:
                getrank_ids = self.getrank_ids_to_list()
                order.getrank_ids = getrank_ids
            if option == 3:
                self.find_kunde()
                kunde_id = int(input("Neuen Kunden nach ID auswählen: "))
                bestellung.kunde_id = kunde_id
            if option == 0:
                break
        self.bestellung_controller.edit_bestellung(bestellung.id, bestellung.kunde_id, bestellung.gericht_ids, bestellung.getrank_ids)
        self.bestellung_controller.recalculate_preis()
        bestellung.calculate_preis()
        print("Die Bestellung wurde bearbeitet", bestellung)

    def gericht_ids_to_list(self):
        gericht_ids = []
        while True:
            print(self.gekochtergericht_controller.view_items())
            print("-1 - Aufhören, Gerichte hinzuzufügen")
            try:
                gericht_id = int(input("Geben Sie das Gericht-ID ein: "))
                if dish_id == -1:
                    break
                elif self.gekochtergericht_controller.validate_id(gericht_id):
                    gericht_ids.append(gericht_id)
                    print("Gericht wurde zu der Bestellung hinzugefügt")
                else:
                    print("Ungültiger Wert")
            except ValueError:
                print("Ungültiger Wert")
        return gericht_ids

    def getrank_ids_to_list(self):
        getrank_ids = []
        while True:
            print(self.getrank_controller.view_items())
            print("-1 - Aufhören, Getränke hinzuzufügen")
            try:
                getrank_id = int(input("Geben Sie die Getränke-ID ein: "))
                if getrank_id == -1:
                    break
                elif self.getrank_controller.validate_id(getrank_id):
                    getrank_ids.append(getrank_id)
                    print("Getränk wurde zu der Bestellung hinzugefügt")
                else:
                    print("Ungültiger Wert")
            except ValueError:
                print("Ungültiger Wert")
        return getrank_ids

    def find_kunde(self):
        print("Suche nach dem neuen Kunden: ")
        search_term = input("Suche: ")
        possible_terms = self.kunde_controller.find_items(search_term)
        print("Unsere aktuellen Kunden sind: \n")
        for term in possible_terms:
            print(term.id, term.name, term.adresse)

    def kunde_id_for_bestellung(self):
        kunde_id = 0
        opt = int(input("""Ist der Kunde neu?
                1 - Ja
                2 - Nein 
                Bitte geben Sie Ihre Auswahl ein: """))
        if opt == 1:
            kunde = neue_kunde()
            self.kunde_controller.add_item(kunde)
            kunde_id = kunde.id
        elif opt == 2:
            self.find_kunde()
            while True:
                kunde_id = input("Kunde ID: ")
                if self.customer_controller.validate_id(customer_id):
                    break
                else:
                    print("Ungültiger Wert")
        return kunde_id

    def add_bestellung_console(self):

        kunde_id = self.kunder_id_for_bestellung()
        gericht_ids = self.gericht_ids_to_list()
        getrank_ids = self.getrank_ids_to_list()
        return Bestellung(kunde_id, gericht_ids, getrank_ids)

    def view_bestellungen(self):
        return self.bestellung_controller.view_items()

    def add_gericht_console(self):
        print("1 - Gekochter Gericht\n2 - Getränk")
        while True:
            try:
                opt = int(input("Rufen Sie die Option: "))
                break
            except ValueError:
                print("Ungültiger Wert")
        if opt == 1:
            while True:
                try:
                    portionsgrosse = input("Portionsgröße: ")
                    preis = int(input("Preis: "))
                    voraussichtlicheLd = int(input("Wie viele Minuten: "))
                    self.gekochtergericht_controller.add_item(CookedDish(portionsgrosse, preis, voraussichtlicheLd))
                    break
                except ValueError:
                    print("Ungültiger Wert")
        if opt == 2:
            while True:
                try:
                    portionsgrosse = input("Portionsgröße: ")
                    preis = int(input("Preis: "))
                    alkoholgehalt = float(input("Alkoholgehalt: "))
                    self.getrank_controller.add_item(Beverage(portionsgrosse, preis, alkoholgehalt))
                    break
                except ValueError:
                    print("Ungültiger Wert")

    def show_rechnung(self):
        print(self.view_bestellungen())
        print("Geben Sie die ID der Bestellung ein, für die Sie die Rechnung sehen möchten: ")
        bestellung_id = int(input("Geben Sie die ID ein: "))
        bestellung = self.bestellung_controller.find_by_id(bestellung_id)
        print(bestellung.show_rechnung())

    def run(self):
        while True:
            print(menu())
            while True:
                try:
                    opt = int(input("Bitte wählen Sie eine Option: "))
                    break
                except ValueError:
                    print("Ungültiger Wert! Bitte wählen Sie eine Zahl")
            if opt == 0:
                break
            if opt == 1:
                self.bestellung_controller.add_item(self.add_bestellung_console())
            if opt == 2:
                print(self.view_bestellungen())
            if opt == 3:
                self.edit_bestellung()
            if opt == 4:
                self.delete_bestellung()
            if opt == 5:
                self.find_kunde()
            if opt == 6:
                self.add_gericht_console()
            if opt == 7:
                self.crud_operations(opt)
            if opt == 8:
                self.crud_operations(opt)
            if opt == 9:
                self.show_rechnung()