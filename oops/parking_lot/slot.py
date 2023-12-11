from interfaces import slot_types, ISlot

class SlotDB:
    def __init__(self):
        self.noof_slots = 2
        self._slots = {}

    def get_slots(self, slot_type):
        if not self._slots.get(slot_type):
            self._slots[slot_type] = self._generate_slots(slot_type)
        return self._slots.get(slot_type)

    def _generate_slots(self, slot_type):
        return [Slot(i, slot_type) for i in range(1, self.noof_slots+1)]

class Slot(ISlot):
    def __init__(self, slot_no, slot_type):
        self.slot_no = slot_no
        self.slot_type = slot_type
        self._vehicle = None

    def is_vacant(self):
        if not self._vehicle:
            return True
        return False        

    def get_vehicle(self):
        return self._vehicle

    def freeze(self, vehicle):
        self._vehicle = vehicle
        vehicle.slot = self

    def release(self):
        self._vehicle = None

slotDB = SlotDB()

def get_slots(type):
    return slotDB.get_slots(type)
