import time
import math
from interfaces import vehicle_types, IVehicle, IVehicleDB

class VehicleDB(IVehicleDB):
    def __init__(self):
        self._vehicles = {}

    def get_vehicles(self):
        return self._vehicles

    def get_vehicle(self, reg_no):
        return self._vehicles.get(reg_no)

    def record_vehicle(self, vehicle):
        self._vehicles[vehicle.reg_no] = vehicle

    def unrecord_vehicle(self, vehicle):
        del self._vehicles[vehicle.reg_no]


class Vehicle(IVehicle):
    def __init__(self, reg_no, vehicle_type):
        self.reg_no = reg_no
        self.vehicle_type = vehicle_type
        self._slot = None
        self.entry_time = None
        self.exit_time = None

    @property
    def slot(self):
        return self._slot

    @slot.setter    
    def slot(self, slot=None):
        self._slot = slot
        if self._slot:
            self.entry_time = time.time() 
            register_vehicle(self)

    def checkout(self):
        self.exit_time = time.time()
        self.slot.release()
        self.slot = None
        unregister_vehicle(self)

    def calculate_fees(self, hourly_price):
        time_spent = self.exit_time-self.entry_time
        return math.ceil(time_spent/(60*60)) * hourly_price
        

_vehicles = VehicleDB()

def get_vehicles():
    return _vehicles.get_vehicles()

def register_vehicle(vehicle):
    _vehicles.record_vehicle(vehicle)

def unregister_vehicle(vehicle):
    _vehicles.unrecord_vehicle(vehicle)

def get_vehicle(reg_no):
    return _vehicles.get_vehicle(reg_no)