from repository.data_repo import DataRepo


class GetrankRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_getrank(self, item_id, portionsgrosse, preis, alkoholgehalt):
        self.items = self.load()
        for item in self.items:
            if item_id == item.id:
                item.portionsgrosse = portionsgrosse
                item.preis = preis
                item.alkoholgehalt = alkoholgehalt
                break
        self.save()