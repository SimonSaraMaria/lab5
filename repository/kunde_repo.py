from repository.data_repo import DataRepo


class KundeRepository(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def edit_kunde(self, customer_id, name, adresse):
        self.items = self.load()
        for item in self.items:
            if customer_id == item.id:
                item.id = customer_id
                item.name = name
                item.adresse = adresse
                break
        self.save()