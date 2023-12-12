from booking import ReservationForm, get_rooms
from rooms import HOTEL_FLOORS, ROOMS_PER_FLOOR, room_types
from guests import get_guests_database

guests = get_guests_database()

# Get all the rooms
rooms = get_rooms()
assert len(rooms) == HOTEL_FLOORS * ROOMS_PER_FLOOR

# Book a room1
room1 = ReservationForm().reserve("bob", "+12345678")
guest1 = room1.guest
assert guest1.name == "bob"
assert guest1.phone_no == "+12345678"
assert room1.is_vacant == False
assert room1.room_no.floor == 0
assert room1.room_no.door == 1

# Get guest1 by phone number
assert guests.getby_phone_no("+12345678") == guest1

# Book room1 for guest2
room = ReservationForm().reserve("Rob", "+1234567890", room_type= room_types.Deluxe, search_algo = "bottom_up")
guest2 = room.guest
assert room.room_type == room_types.Deluxe


# Vacate a room
guest1.vacate()
assert room1.is_vacant == True