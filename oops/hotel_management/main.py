from booking import ReservationForm, get_rooms
from rooms import HOTEL_FLOORS, ROOMS_PER_FLOOR
from guests import get_guests_database

guests = get_guests_database()

# Get all the rooms
rooms = get_rooms()
assert len(rooms) == HOTEL_FLOORS * ROOMS_PER_FLOOR

# Book a room
room = ReservationForm().reserve("bob", "+12345678")
guest = room.guest
assert guest.name == "bob"
assert guest.phone_no == "+12345678"
assert room.is_vacant == False
guests.add_guest(guest)

# Get guest by phone number
assert guests.getby_phone_no("+12345678") == guest

# Vacate a room
guest.vacate()
assert room.is_vacant == True