from controller import Controller


class BestellungController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def validate_gericht_id(self, gericht_id, gericht_option):
        """
        When a dish is deleted, the method is used to verify if all the ids in the Orders still exist
        :param dish_id: the id of the dish that was deleted
        :param dish_option: Option that checks if the dish is a Cooked Dish(1) or a Beverage(2)
        :return:
        """
        items = self.repo.read()
        for item in items:
            if int(gericht_option) == 1:
                element_count = item.gericht_ids.count(gericht_id)
                while element_count > 0:
                    item.gericht_ids.remove(gericht_id)
                    element_count -= 1
            if int(gericht_option) == 2:
                element_count = item.getrank_ids.count(gericht_id)
                while element_count > 0:
                    item.getrank_ids.remove(gericht_id)
                    element_count -= 1
        self.repo.save()

    def recalculate_preis(self):
        """
        Calculates the price of all the orders that are saved in the file
        :return:
        """
        items = self.repo.read()
        for item in items:
            item.calculate_preis()
        self.repo.save()

    def validate_kunde_id(self, kunde_id):
        """
        When a customer is deleted, then the method also deletes all the orders that were associated with that customer
        :param customer_id: the id of the customer that was just deleted
        :return:
        """
        items = self.repo.read()
        for item in items:
            if int(kunde_id) == int(item.kunde_id):
                self.delete_item(item.id)

    def edit_order(self, item_id, kunde_id, gericht_ids, getrank_ids):
        self.repo.edit_bestellung(item_id, kunde_id, gericht_ids, getrank_ids)
