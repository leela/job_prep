from role import get_role, get_role_category
from billing import get_billing_type
from report import get_report

class Employee:
    def __init__(self, id, name, role, hour_price) -> None:
        self.id = id
        self.name = name
        self.role = get_role(role)
        self.hour_price = hour_price
        self.billing_type = get_billing_type()
        self.role_category = get_role_category(role)

    def calculate_salary(self):
        hours_worked = self.get_report()['work_hours']
        self.billing_type.track_hours(hours_worked)
        return self.billing_type.calculate_salary(self.hour_price)

    def get_report(self):
        return get_report(self)
