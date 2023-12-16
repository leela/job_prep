from collections import Counter
from data_storage import DictStorage

from custom_exceptions import DuplicateColumnError, DataValidationError

class CreateDB:
    def __init__(self, dbname):
        self.dbname = dbname
        self.tables = {}

    def create_table(self, tname, columns):
        if self._is_table_exists(tname):
            raise

        table = Table.create_table(tname, columns)
        self.tables[tname] = table
        print(f"Table named '{tname}' is created.")
        return table

    def delete_table(self, tname):
        return self.tables.pop(tname)        

    def _is_table_exists(self, tname):
        return tname in self.tables


class Table:
    def __init__(self, tname, columns):
        self.tname = tname
        self.columns = columns
        self.tdata = DictStorage()

    def insert(self, **kwargs):
        self.validate(**kwargs)
        self.tdata.add_record(**kwargs)

    def validate(self, **kwargs):        
        errors_by_column = {}
        error_count = 0
        for column in self.columns:
            errors = column.validate(kwargs.get(column.cname))
            error_count += len(errors)
            errors_by_column[column] = errors
        if error_count:
            # TODO: Instead of raising, print the error messages.
            raise DataValidationError(errors_by_column)

    def select_all(self):
        return self.tdata.select_all()

    def filter(self, by_columns):
        return self.tdata.filter(by_columns)

    @classmethod
    def create_table(cls, tname, columns):
        cls._validate_schema(columns)
        return cls(tname, columns)
    
    @staticmethod
    def _validate_schema(columns):
        col_names = [c.cname for c in columns]
        unique_col_names = set(col_names)
        dup_col_names = (Counter(col_names) - Counter(unique_col_names)).keys()
        if dup_col_names:
            raise DuplicateColumnError(f"{','.join(dup_col_names)} repeated for more than one column.")