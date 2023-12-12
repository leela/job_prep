from enum import Enum
from abc import ABC, ABCMeta, abstractmethod

slot_types = Enum("SlotType", ["TWO_WHEELER", "FOUR_WHEELER"])
vehicle_types = slot_types

class ISlot(ABC):
    @abstractmethod
    def freeze(self):
        pass

    @abstractmethod
    def release(self):
        pass


class IVehicleDB(ABC):
    @abstractmethod
    def get_vehicles(self):
        pass

    @abstractmethod
    def record_vehicle(self):
        pass

    @abstractmethod
    def unrecord_vehicle(self):
        pass


class IVehicle(ABC):
    @property
    @abstractmethod
    def slot(self):
        pass

    @slot.setter
    @abstractmethod
    def slot(self):
        pass

    @abstractmethod
    def checkout(self):
        pass

    @abstractmethod
    def calculate_fees(self, hourly_fees):
        pass