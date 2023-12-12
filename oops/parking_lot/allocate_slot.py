from slot import get_slots


class SlotUnavailable(Exception):
    pass

class SlotAlgo:
    def __init__(self, slots):
        self.slots = slots

    def get_empty_slot(self):
        for slot in self.slots:
            if slot.is_vacant():
                return slot


class SlotManager:
    """Allocate the slot to a vehicle
    """
    def allocate_slot(self, vehicle):
        algo = SlotAlgo(get_slots(vehicle.vehicle_type))
        slot = algo.get_empty_slot()
        if not slot:
            raise SlotUnavailable("Sorry! All slots are occupied.")
        slot.freeze(vehicle)
        return slot