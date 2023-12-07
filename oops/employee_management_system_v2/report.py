from interfaces import ICRole, SupervisorRole
from abc import ABC, abstractmethod

class ReportSystem:
    def __init__(self):
        self._report_category = {
            ICRole: ICReport,
            SupervisorRole: SupervisorReport
        }

    def get_report_category(self, role_category):
        return self._report_category[role_category]

class Report:
    def __init__(self, reportee):
        self.reportee = reportee

    @abstractmethod
    def work_hours(self):
        pass

    def get_report(self):
        return {
            "name": self.reportee.name,
            "work_hours": self.work_hours()
        }

class ICReport(Report):
    def work_hours(self):
        return len(self.reportee.role.work())
    
class SupervisorReport(Report):
    def work_hours(self):
        total_work_hours = 0
        for reportee in self.reportee.role.get_reportees():
            total_work_hours += reportee.get_report().get("work_hours")
        return total_work_hours * 0.25
    

def get_report(employee):
    report_category = ReportSystem().get_report_category(employee.role_category)
    return report_category(employee).get_report()

def get_reportees_report(manager):
    reports = []
    for reportee in manager.role.get_reportees():
        reports.append(get_report(reportee))
    return reports