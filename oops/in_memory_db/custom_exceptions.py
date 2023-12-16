class DuplicateColumnError(Exception):
    pass

class DataValidationError(Exception):
    pass

class ValueRequiredError(Exception):
    pass

class OutOfRangeError(Exception):
    pass

class MaxLengthError(Exception):
    pass

class DataValidationError(Exception):
    def __init__(self, error_list, *args, **kwargs):
        message = error_list
        print("="*40)
        for column, errors in error_list.items():
            if errors:
                print(f"{column.cname}: {[e.args[0] for e in errors]}")
        print("="*40)
        super().__init__(self, "Data is not valid.", *args, **kwargs)