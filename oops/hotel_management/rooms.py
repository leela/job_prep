from collections import namedtuple

HOTEL_FLOORS = 4
ROOMS_PER_FLOOR = 100

RoomNumber = namedtuple('Point', ['floor', 'door'])

class _RoomDatabase:
    def __init__(self, rooms):
        self._rooms = rooms

    def get_rooms(self):
        return self._rooms

    @classmethod
    def _generate_rooms(cls, noof_floors=HOTEL_FLOORS, rooms_per_floor=ROOMS_PER_FLOOR):
        room_nos = [RoomNumber(floor, door) for floor in range(noof_floors) for door in range(1, rooms_per_floor+1)]
        rooms = [Room(room_no) for room_no in room_nos]
        for room in rooms:
            room.vacate()

        return cls(rooms)

class Room:
    def __init__(self, room_no):
        self.room_no = room_no
        self.is_vacant = None
        self.guest = None

    def occupy(self, guest):
        self.is_vacant = False
        self.guest = guest

    def vacate(self):
        self.guest = None
        self.is_vacant = True


room_database = _RoomDatabase._generate_rooms()

def get_all_rooms():
    return room_database.get_rooms()