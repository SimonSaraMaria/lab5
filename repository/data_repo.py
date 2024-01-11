import pickle
import ast


class DataRepo:
    def __init__(self, filename):
        self.filename = filename
        self.items = []
        self.load()

    def save(self):
        """
        Uses pickle to write a binary file
        :return:
        """
        f = open(self.filename, 'wb')
        pickle.dump(self.items, f)

        f.close()

    def load(self):
        """
        Uses pickle to return the items from a binary file
        :return: Returns a list of all the items in the file
        """
        try:
            f = open(self.filename, 'rb')
            self.items = pickle.load(f)
            f.close()
        except:
            self.items = []
        return self.items

    def read(self):
        """
        :return: the items that are saved in a file
        """
        self.load()
        return self.items

    def add_item(self, item):
        """
        Adds a new item to the file
        :param item: The item to be added
        :return:
        """
        self.items.append(item)
        self.save()

    def convert_to_string(self, obj_list):
        obj_string_list = map(lambda x: pickle.dumps(x), obj_list)
        return list(obj_string_list)

    def convert_from_string(self, obj_string_list):
        obj_list = map(lambda x: pickle.loads(ast.literal_eval(x)), obj_string_list)
        return list(obj_list)

    def read_file(self, filename=None):
        """
        Reads a non-binary file
        :param filename: is used to decide where to write at
        :return:
        """
        if filename is None:
            self.read()
        else:
            f = open(filename, 'r')
            text = []
            for line in f:
                text.append(line)
            f.close()
            return text

    def write_file(self, text, filename=None):
        """
        Writes to non-binary file
        :param text: the text that should be added
        :param filename: the file to write to
        :return:
        """
        if filename is None:
            filename = self.filename
        else:
            f = open(filename, 'w')
            f.write(text)

    def delete_item(self, item_id):
        """
        Deletes the item by the id they have
        :param item_id: the id of the item that is supposed to be deleted
        :return:
        """
        f = open(self.filename, 'rb')
        self.items = pickle.load(f)
        f.close()
        self.items = list(filter(lambda item: item.id != item_id, self.items))
        self.save()

    def validate_id(self, proposed_id):
        try:
            proposed_id = int(proposed_id)
        except ValueError:
            return False
        for item in self.items:
            if item.id == proposed_id:
                return True
        return False