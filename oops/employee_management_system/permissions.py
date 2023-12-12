
class _RoleDatabse:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "designer": DesignerRole,
            "developer": DeveloperRole
        }

    def get_role(self, role_name):
        role = self._roles.get(role_name)
        if role:
            return role()
        else:
            raise TypeError("Role does not exist.")
    

class _Role:
    def can_add_reportee(self, reportee_role=None):
        return False

    def can_view_reportees(self):
        return True

class ManagerRole(_Role):
    def __init__(self):
        super().__init__()
        self._reportee_roles = [DesignerRole, DeveloperRole, ManagerRole]

    def can_add_reportee(self, reportee_role=None):
        return reportee_role.__class__ in self._reportee_roles

class DesignerRole(_Role):
    pass

class DeveloperRole(_Role):
    pass


role_database = _RoleDatabse()

def get_role(role_name):
    return role_database.get_role(role_name)