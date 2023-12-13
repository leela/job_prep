from exceptions import LimitExceedError, BookUnavailableError
from utils import Collection
ALLOWED_ACTIVE_USERS = 1
    


class User:
    def __init__(self):
        self._books = Collection()
        users.add_user(self)
                
    def lend_book(self, book):
        """Lending is equalent to reading a book for now.
        """
        if self.is_active():
            raise  LimitExceedError("Please return before lending new.")

        if not book.can_lent():
            raise BookUnavailableError("Book is not available at this moment.")

        if not users.can_add_active_user():
            raise LimitExceedError("We do not allow more users at this moment.")

        # Add to users shelf
        self._books.add_item(book)

        # Remove from book shelf
        book.add_lender(self)

    def return_book(self, book):
        # Add to the book shelf
        book.remove_lender(self)

        #Remove from user shelf
        self._books.remove_item(book)

    def is_active(self):
        return bool(self._books.collection)
    
class _Users:
    def __init__(self) -> None:
        self._users = set()

    @property
    def users(self):
        return self._users
    
    def add_user(self, user):
        self._users.add(user)

    def remove_user(self, user):
        self._users.discard(user)

    def get_active_users(self):
        return [user for user in self._users if user.is_active()]

    def can_add_active_user(self):
        return len(self.get_active_users()) < ALLOWED_ACTIVE_USERS

users = _Users()