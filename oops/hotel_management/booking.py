from guests import Guest
from rooms import get_rooms
from room_search import get_empty_room

class UnavailableError(Exception):
    pass

class ReservationForm:
    def reserve(self, name, phone_no):
        room = get_empty_room(get_rooms())
        if room:
            guest = Guest(name, phone_no)
            room.occupy(guest)
            guest.set_room(room)
        else:
            raise UnavailableError("Room are full")
        return room
    
class Operator:
    pass