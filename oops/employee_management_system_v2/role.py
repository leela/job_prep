from abc import ABC, abstractmethod
from interfaces import ICRole, SupervisorRole

class RoleMapper:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "developer": DeveloperRole,
            "designer": DesignerRole
        }

    def get_role(self, role_name):
        return self._roles.get(role_name)

    def get_role_category(self, role_name):
        role = self.get_role(role_name)
        if role in ICRole.__subclasses__():
            return ICRole
        elif role in SupervisorRole.__subclasses__():
            return SupervisorRole


class ManagerRole(SupervisorRole):
    def __init__(self):
        self._reportees = []

    def add_reportee(self, reportee):
        self._reportees.append(reportee)

    def get_reportees(self):
        return self._reportees

class DeveloperRole(ICRole):
    def work(self):
        return "Developer: Completed X module"

class DesignerRole(ICRole):
    def work(self):
        return "Designer: Completed X, y and Z module"


def get_role(role_type):
    return RoleMapper().get_role(role_type)()

def get_role_category(role_type):
    return RoleMapper().get_role_category(role_type)