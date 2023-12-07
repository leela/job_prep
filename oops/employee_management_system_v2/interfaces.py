from abc import ABC, abstractmethod

class ICRole(ABC):
    @abstractmethod
    def work(self):
        pass

class SupervisorRole(ABC):
    @abstractmethod
    def add_reportee(self):
        pass

    @abstractmethod
    def get_reportees(self):
        pass
