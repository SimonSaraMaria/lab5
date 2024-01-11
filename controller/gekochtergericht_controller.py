from controller import Controller


class GekochterGerichtController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def edit_gekochtergericht(self, gekochtergericht_id, portionsgrosse, preis, voraussichtlicheLd):
        self.repo.edit_gekochtergericht(gekochtergericht_id, portionsgrosse, preis, voraussichtlicheLd)