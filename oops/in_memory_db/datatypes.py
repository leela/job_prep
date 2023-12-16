from constraints import LengthConstraint, RangeConstraint, RequiredConstraint

class Column:
    validations = []
    def __init__(self, cname, **kwargs):
        self.cname = cname
        self.extra_args = kwargs

    def _extra_validations(self):
        extra = []
        if self.extra_args.get("is_required"):
            extra.append(RequiredConstraint())
        return extra

    def _get_validations(self):
        return self._extra_validations() + self.validations

    def validate(self, value):
        errors = []
        for v in self._get_validations():
            try:
                v.validate(value)
            except Exception as e:
                errors.append(e)
        return errors

class StringColumn(Column):
    validations = [LengthConstraint()]

class IntegerColumn(Column):
    validations = [RangeConstraint()]
