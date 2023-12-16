from search import DictSearchAlgo

class DictStorage:
    search_algo = DictSearchAlgo

    def __init__(self):
        self._data = []

    def add_record(self, **kwargs):
        self._data.append(kwargs)

    # Select data
    def select_all(self):
        return self.search_algo(self._data).select_all()

    def filter(self, match_columns):
        return self.search_algo(self._data).filter(match_columns)
    
