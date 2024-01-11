from controller import Controller


class GetrankController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def edit_getrank(self, getrank_id, portionsgrosse, preis, alkoholgehalt):
        self.repo.edit_getrank(getrank_id, portionsgrosse, preis, alkoholgehalt)
