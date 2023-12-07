class Guest:
    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no
        self.booking_data = None
        self.room = None

    def set_room(self, room):
        self.room = room

    def vacate(self):
        self.room.vacate()


class GuestDS:
    def __init__(self):
        self.data = {}

    def _build_data(self, guests):
        for guest in guests:
            self.data[guest.phone_no] = guest

    def getby_phone_no(self, phone_no):
        return self.data.get(phone_no)

    @classmethod
    def build_guestDS(cls, guests):
        ds = cls()
        ds._build_data(guests)
        return ds
    
    def add_guest(self, guest):
        self._build_data([guest])

    def remove_guest(self, guest):
        del self.data[guest.phone_no]


def get_guests_database():
    return GuestDS()