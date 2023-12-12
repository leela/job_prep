from abc import ABC, abstractmethod
from collections import namedtuple

class RoomSearchSystem:
    def __init__(self):
        self.algos = {
            "round_robin": RoundRobinRoomSearch(),
            "bottom_up": BottomUpRoomSearch()
        } 

    def _get_search_algo(self, algo):
        return self.algos.get(algo)

class RoomSearch(ABC):
    @abstractmethod
    def _build_data(self, rooms):
        pass

    @abstractmethod
    def find_empty(self):
        pass

class RoundRobinRoomSearch(RoomSearch):
    def __init__(self):
        self._rooms = []

    def _build_data(self, rooms):
        self._rooms = rooms

    def find_empty(self):
        for room in self._rooms:
            if room.is_vacant:
                return room
            
class BottomUpRoomSearch(RoomSearch):
    def __init__(self):
        self._rooms_dict = None
        self._sorted_room_nos = None

    def _build_data(self, rooms):
        self._rooms_dict = {r.room_no: r for r in rooms}
        self._sorted_room_nos = named_tuple_sort(self._rooms_dict.keys(), ["floor", "door"])

    def find_empty(self):
        for room_no in self._sorted_room_nos:
            room = self._rooms_dict[room_no]
            if room.is_vacant:
                return room

def named_tuple_sort(items, sort_order):
    """
    number_by_place = namedtuple("number_by_place", ["tens", "ones"])
    numbers = [number_by_place(x, y) for x in [3,2,1,4] for y in [2,1,3,5,4,6,8,7]]
    >>> named_tuple_sort(numbers, ["tens", "ones"])
    """
    res = items
    for each in sort_order:
        res = sorted(res, key=lambda item: getattr(item, each))
    return res

def get_vacant_room(rooms, search_algo="round_robin"):
    search_algo = RoomSearchSystem()._get_search_algo(search_algo)
    search_algo._build_data(rooms)
    return search_algo.find_empty()