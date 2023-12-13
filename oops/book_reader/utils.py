class Collection:
    """
    Requirement: Every item should have "name" attribute to use this object.
    """
    def __init__(self):
        self._collection = {}

    @property
    def collection(self):
        return self._collection

    def add_item(self, item):
        self._collection[item.name] = item

    def remove_item(self, item):
        del self._collection[item.name]

    def search(self, name):
        return self._collection.get(name)
