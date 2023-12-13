import books
from  user import User, users
import user
from exceptions import LimitExceedError, BookUnavailableError

# Search for a book named "Odyssey"
book1 = books.get_book("Odyssey")
book2 = books.get_book("Romeo and Juliet")
assert book1.name == "Odyssey"


# user reading a book
user1 = User()
assert  book1.can_lent()
user1.lend_book(book1)
assert not book1.can_lent()
assert user1.is_active()

# User1 should not be able to lend books while active
try:
    user1.lend_book(book2)
except LimitExceedError:
    pass

# Return a book and lend new book
user1.return_book(book1)
assert book1.can_lent()
assert not user1.is_active()
user1.lend_book(book2)
assert not book2.can_lent()
assert user1.is_active()

# Get active users
print(users.get_active_users())

# Check that we can not have more than one active user. 
user2 = User()
try:
    user2.lend_book(book1)
except LimitExceedError:
    pass

assert book1.can_lent()
assert user2 in users.users
assert user2 not in users.get_active_users()

# Check that we can have 2 active users and allow 2 readers to read a book
books.NOOF_PARALLEL_READERS_PER_BOOK = 2
user.ALLOWED_ACTIVE_USERS = 2

assert book2.can_lent()

user2 = User()
user2.lend_book(book2)

assert not book2.can_lent()
assert user2 in users.users
assert user2 in users.get_active_users()
