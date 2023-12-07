from rooms import Room
from guests import Guest

class GuestDatabase:
    def __init__(self):
        self.guests_data = [
                        {
                'name': 'Sid',
                'phone_no': '+910123456789',
                'room': 10
            },
            {
                'name': 'Vid',
                'phone_no': '+911234567890',
                'room': 110
            },
            {
                'name': 'Rid',
                'phone_no': '+912345678901',
                'room': 210

            },
            {
                'name': 'Lid',
                'phone_no': '+913456789012',
                'room': 310
            },
            {
                'name': 'Mid',
                'phone_no': '+914567890123',
                'room': 290
            }
        ]
        self.guests = []

    def _generate_guest_database(self):
        for data in self.guests_data:
            guest = Guest(data['name'], data['phone_no'])
            room = Room(data['room'])
            room.occupy(guest)
            guest.set_room(room)
            self.guests.append(guest)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest():
        pass

    def get_guests(self):
        if not self.guests:
            self._generate_guest_database()
        return self.guests

guests_db = GuestDatabase()        

def get_guests():
    return guests_db.get_guests()