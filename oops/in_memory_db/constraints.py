from collections import namedtuple
from custom_exceptions import ValueRequiredError, OutOfRangeError, MaxLengthError

IntRange = namedtuple("IntRange", ("min", "max"))
INT_RANGE = IntRange(-1024, 1024)
MAX_STR_LENGTH = 20

class Constraint:
    def validate(self):
        pass

class LengthConstraint(Constraint):
    def __init__(self, max_length = MAX_STR_LENGTH):
        self.max_length = max_length

    def validate(self, value):
        if value and  not (len(value) <= self.max_length):
            raise MaxLengthError(f"Maximum allowed length is {self.max_length}")

class RangeConstraint(Constraint):
    def __init__(self, min=INT_RANGE.min, max=INT_RANGE.max):
        self.min = min
        self.max = max

    def validate(self, value):
        if value and not (self.min <= value <= self.max):
            raise OutOfRangeError(f"Value has to be in ({self.min}, {self.max}) range")

class RequiredConstraint(Constraint):
    def validate(self, value):
        if value is None:
            raise ValueRequiredError("Field is required.")
