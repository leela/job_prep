from guests import Guest
from rooms import get_all_rooms
from room_search import get_empty_room

class UnavailableError(Exception):
    pass

class ReservationForm:
    def reserve(self, name, phone_no, search_room_by = "round_robin"):
        room = get_empty_room(get_all_rooms(), search_room_by)
        if room:
            guest = Guest(name, phone_no)
            room.occupy(guest)
            guest.set_room(room)
        else:
            raise UnavailableError("Rooms are full")
        return room
    
class Operator:
    pass