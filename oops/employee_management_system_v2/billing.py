class BillingSystem:
    def __init__(self):
        self.hours_worked = 0

    def track_hours(self, hours_worked):
        self.hours_worked += hours_worked

class HourlyEmployee(BillingSystem):
    def calculate_salary(self, hour_price):
        return self.hours_worked * hour_price
    
def get_billing_type():
    return HourlyEmployee()