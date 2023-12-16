from abc import ABC, abstractmethod

class SearchAlgo(ABC):
    @abstractmethod
    def select_all(self):
        pass

    @abstractmethod
    def filter(self, match_columns):
        pass

class DictSearchAlgo(SearchAlgo):
    def __init__(self, data):
        self.data = data

    def select_all(self):
        return self.data[:]

    def filter(self, match_columns=None):
        if not match_columns:
            return self.selct_all()

        res = []
        for record in self.data:
            for col, value in match_columns.items():
                if record.get(col) != value:
                    break
            else:
                res.append(record)
        return res
