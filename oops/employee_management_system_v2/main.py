from employees import Employee
from report import get_reportees_report

hour_price = 1000

manager1 = Employee("1", "Manager_First", "manager", hour_price)
manager2 = Employee("2", "Manager_Two", "manager", hour_price)
manager3 = Employee("2", "Manager_Three", "manager", hour_price)

# create designer with manager
designer1 = Employee("3", "Designer_First", "designer", hour_price)
manager1.role.add_reportee(designer1)
assert designer1 in manager1.role.get_reportees()
designer1.role.work()

# Create developer without manager and add manager
developer1 = Employee("4", "Developer-First", "developer", hour_price)
manager2.role.add_reportee(developer1)
developer1.role.work()
assert developer1 in manager2.role.get_reportees()

# Add manager to manager
manager3.role.add_reportee(manager1)
assert manager1 in manager3.role.get_reportees()

#Get manager1 reportees report
print(get_reportees_report(manager1)) 

#Get manager3 reportees report
print(get_reportees_report(manager3)) 
