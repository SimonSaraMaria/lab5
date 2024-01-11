from repository.data_repo import DataRepo


class GekochterGerichtRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_gekochtergericht(self, item_id, portionsgrosse, preis, voraussichtlicheLd):
        self.items = self.load()
        for item in self.items:
            if item_id == item.id:
                item.portionsgrosse = portion_size
                item.preis = preis
                item.voraussichtlicheLd = voraussichtlicheLd
                break
        self.save()