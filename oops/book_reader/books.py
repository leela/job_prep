
from utils import Collection

NOOF_PARALLEL_READERS_PER_BOOK = 1

sample_books = [
        {"name": "Romeo and Juliet", "author": "William Shakespeare"},
        {"name": "Farm House", "author": "George Orwell"},
        {"name": "Alice in Wonderland", "author": "Lewis Carrol"},
        {"name": "The room on the roof", "author": "Ruskin bond"},
        {"name": "Odyssey", "author": "Homer"},
]

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self._users = set()

    def can_lent(self):
        return len(self._users) < NOOF_PARALLEL_READERS_PER_BOOK

    def remove_lender(self, user):
        self._users.discard(user)

    def add_lender(self, user):
        self._users.add(user)


def get_sample_books():
    books = []
    for each in sample_books:
        books.append(Book(each['name'], each['author']))
    return books


books = Collection()

for book in get_sample_books():
    books.add_item(book)

def get_book(book_name):
    return books.search(book_name)