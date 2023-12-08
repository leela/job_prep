from collections import namedtuple
from enum import Enum
import random

HOTEL_FLOORS = 4
ROOMS_PER_FLOOR = 100

room_types = Enum("RoomTypes", ["Regular", "Deluxe", "Luxury"])
RoomNumber = namedtuple('Point', ['floor', 'door'])


class _RoomDatabase:
    def __init__(self, rooms):
        self._rooms = rooms

    def get_rooms(self):
        return self._rooms
    
    def get_by_room_type(self, room_type):
        return [room for room in self.get_rooms() if room.room_type==room_type]

    @classmethod
    def _generate_rooms(cls, noof_floors=HOTEL_FLOORS, rooms_per_floor=ROOMS_PER_FLOOR):
        room_nos = [RoomNumber(floor, door) for floor in range(noof_floors) for door in range(1, rooms_per_floor+1)]
        rooms = [Room(room_no) for room_no in room_nos]
        for room in rooms:
            room.vacate()
            room.room_type = random.choice(list(room_types))
        return cls(rooms)

class Room:
    def __init__(self, room_no, room_type=room_types.Regular):
        self.room_no = room_no
        self.is_vacant = None
        self.guest = None
        self.room_type = room_type

    def occupy(self, guest):
        self.is_vacant = False
        self.guest = guest

    def vacate(self):
        self.guest = None
        self.is_vacant = True


room_database = _RoomDatabase._generate_rooms()

def get_all_rooms():
    return room_database.get_rooms()

def get_rooms(room_type=None):
    if not room_type:
        return get_all_rooms()
    return room_database.get_by_room_type(room_type)