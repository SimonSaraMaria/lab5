class Controller:

    def __init__(self, repo):
        self.repo = repo

    def add_item(self, item):
        self.repo.add_item(item)

    def view_items(self):
        return self.repo.read()

    def find_by_id(self, item_id):
        items = self.repo.read()
        # return filter(lambda item: item_id == item.id, items)
        for item in items:
            if int(item.id) == int(item_id):
                return item
        return None

    def delete_item(self, item_id):
        self.repo.delete_item(item_id)

    def validate_id(self, proposed_id):
        return self.repo.validate_id(proposed_id)