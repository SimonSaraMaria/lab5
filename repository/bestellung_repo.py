from repository.data_repo import DataRepo


class BestellungRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_bestellung(self, item_id, kunde_id, gericht_ids, getrank_ids):
        self.items = self.load()
        for item in self.items:
            if item_id == item.id:
                item.kunde_id = kunde_id
                item.gericht_ids = gericht_ids
                item.getrank_ids = getrank_ids
                item.calculate_preis()
                break
        self.save()


