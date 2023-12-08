from guests import Guest
from rooms import get_rooms
from room_search import get_vacant_room

class UnavailableError(Exception):
    pass

class ReservationForm:
    def reserve(self, name, phone_no, room_type=None, search_algo = "round_robin"):
        rooms = get_rooms(room_type=room_type)
        room = get_vacant_room(rooms, search_algo)
        if room:
            guest = Guest(name, phone_no)
            room.occupy(guest)
            guest.set_room(room)
        else:
            raise UnavailableError("Rooms are full")
        return room
    
class Operator:
    pass