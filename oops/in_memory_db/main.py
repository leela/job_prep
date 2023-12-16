from db_entities import CreateDB
from datatypes import StringColumn, IntegerColumn


def main():
    db = CreateDB("book_reader")

    book_name_column = StringColumn(cname = "book_name", is_required = True)
    author_name_column = StringColumn(cname="author_name", is_required = True)
    noof_pages_column =  IntegerColumn(cname = "noof_pages")

    columns = [book_name_column, author_name_column, noof_pages_column]
    table = db.create_table("books", columns)

    # Insert record
    # table.insert(book_name="a"*100, author_name="b"*100, noof_pages=100000)
    table.insert(book_name="Romeo and Juliet", author_name="William Shakespeare", noof_pages=100)
    table.insert(book_name="Farm House", author_name="George Orwell", noof_pages=200)
    table.insert(book_name="The room on the roof", author_name="Ruskin bond", noof_pages=300)
    table.insert(book_name="Hamlet", author_name="William Shakespeare", noof_pages=400)

    print(table.select_all())
    print("-"*20)
    print(table.filter({"author_name": "William Shakespeare", "book_name": "Romeo and Juliet"}))

    db.delete_table(table.tname)
    print(db.tables)

if __name__ == "__main__":
    main()