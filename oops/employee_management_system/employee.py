import permissions

class ReporteeError(Exception):
    pass

class Employee:
    def __init__(self, id, name, role, manager):
        self.id = id
        self.name = name
        self.role = role
        self.manager = manager
        self._reportees = []

    def work(self):
        print(f"Working as {self.role}")

    def add_reportee(self, reportee):
        reportee.manager = self

    @property
    def manager(self):
        return self._manager
    
    @manager.setter
    def manager(self, boss):
        if boss and boss.role.can_add_reportee(self.role):
            self._manager = boss
            boss._reportees.append(self)
        elif boss:
            raise ReporteeError(f"Can not add {self.role} as a reportee to {boss.role}")
        else:
            self._manager = None

    @property
    def reportees(self):
        return self._reportees

    @staticmethod
    def create_employee(id, name, role_name, boss=None):
        """
        TODO:
        * Change manager object into manager_id, when there is Employee database 
        """
        role = permissions.get_role(role_name)
        return Employee(id, name, role, boss)
    
    def __repr__(self):
        return f"Employee({self.id}, {self.name})"


if __name__ == "__main__":
    manager1 = Employee.create_employee("1", "Manager_First", "manager")
    manager2 = Employee.create_employee("2", "Manager_Two", "manager")

    # create designer with manager
    designer1 = Employee.create_employee("3", "Designer_First", "designer", boss = manager1)
    assert manager1._reportees == [designer1]

    # Create developer without manager and add manager
    developer1 = Employee.create_employee("4", "Developer-First", "developer")
    developer1.manager = manager2
    assert developer1.manager == manager2
    assert developer1  in manager2._reportees

    # Add boss to the manager
    manager2.manager = manager1
    assert manager2 in manager1._reportees