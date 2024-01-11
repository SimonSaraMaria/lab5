from controller import Controller


class KundeController(Controller):
    def __init__(self, repo):
        super().__init__(repo)

    def find_items(self, search_term):
        items = self.repo.read()
        return filter(lambda item:
                      search_term.lower() in item.name.lower() or search_term.lower() in item.address.lower(), items)


    def edit_kunde(self, kunde_id, name, adresse):
        self.repo.edit_kunde(kunde_id, name, adresse)