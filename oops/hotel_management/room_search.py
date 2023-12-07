class RoomSearchDS:
    def __init__(self, rooms):
        self.rooms = rooms

    def find_empty(self):
        for room in self.rooms:
            if room.is_vacant:
                return room
            

def get_empty_room(rooms):
    room_search = RoomSearchDS(rooms)
    return room_search.find_empty()