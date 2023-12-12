from allocate_slot import SlotManager
from vehicle import Vehicle, get_vehicle
from interfaces import vehicle_types

slot_manager = SlotManager()

# Allocate a slot for a vehicle "TN05AB1234"
car1 = Vehicle("TN00CA1234", vehicle_types.FOUR_WHEELER)
slot1 = slot_manager.allocate_slot(car1)
assert slot1 == slot1.get_vehicle().slot
print(slot1)

car2 = Vehicle("TN00CA1235", vehicle_types.FOUR_WHEELER)
slot2 = slot_manager.allocate_slot(car2)
assert slot2 == slot2.get_vehicle().slot
print(slot2)

# Get slot of a car1
assert slot1 == get_vehicle("TN00CA1234").slot

# Checkout the vehicle
assert get_vehicle(car2.reg_no) == car2
car2.checkout()
print("Parking charges: ", car2.calculate_fees(10))
assert get_vehicle(car2.reg_no) == None

