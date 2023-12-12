from interfaces import slot_types, ISlot
from utils import flatten_dict

parking_spaces = {
    "space_name1": { #Space name
        1: {        # floor number
            slot_types.TWO_WHEELER: 1, # slot_type: #of slots
            slot_types.FOUR_WHEELER: 1
        }
    },
    "space_name2": {
        -1: {
            slot_types.TWO_WHEELER: 1,
        }, 
        0: {
            slot_types.FOUR_WHEELER: 1
        },
    },
    "space_name3": {
        0: {
            slot_types.FOUR_WHEELER: 1
        }
    }
}

class SlotDB:
    def __init__(self):
        self.noof_slots = 2
        self._slots = {}

    def get_slots(self, slot_type):
        if not self._slots.get(slot_type):
            self._slots[slot_type] = self._generate_slots(slot_type)
        return self._slots.get(slot_type)

    def _filter_spaces_by_slot_type(self, slot_type):
        fl_parking_spaces = flatten_dict(parking_spaces)
        filter_fun = lambda x: x[2]==slot_type
        filtered_spaces = filter(filter_fun, fl_parking_spaces)
        return {space: fl_parking_spaces[space] for space in filtered_spaces}

    def _generate_slots(self, slot_type):
        slots = []
        filtered_spaces = self._filter_spaces_by_slot_type(slot_type)
        for space, noof_lots in filtered_spaces.items():
            space_name, floor_no, _ = space
            slots.extend(
                [Slot(slot_type, i, floor_no, space_name) for i in range(1, noof_lots+1)]
            )
        return slots

class Slot(ISlot):
    def __init__(self, slot_type, slot_no, floor_no=None, space_name=None):
        self.slot_no = slot_no
        self.floor_no = floor_no
        self.space_name = space_name
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
    
    def __str__(self):
        return f"Slot: ({self.space_name}, {self.floor_no}, {self.slot_no})"

slotDB = SlotDB()

def get_slots(type):
    return slotDB.get_slots(type)
