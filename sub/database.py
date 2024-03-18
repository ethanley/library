import os.path
from sub.book import Book

class Database:
    __FILE_NAME = "./database/books.csv"

    @classmethod
    def filepath(cls):
        return os.path.abspath(cls.__FILE_NAME)

    @classmethod
    def is_initialised(cls):
        return os.path.isfile(cls.__FILE_NAME)

    @classmethod
    def initialise(cls, books = []):
        with open(cls.__FILE_NAME, "w") as file:
            for book in books:
                table_row = book.map_to_table_row() + "\n"
                file.write(table_row)

    @classmethod
    def get_all_books(cls):
        if (not cls.is_initialised()):
            cls.initialise()

        with open(cls.__FILE_NAME, "r") as file:
            data = file.read()

        rows = data.split('\n')
        books = [Book.map_table_row_to_book(row) for row in rows if row != '']

        return books

    @classmethod
    def add_book(cls, book):
        table_row = book.map_to_table_row()

        if (not cls.is_initialised()):
            cls.initialise()

        with open(cls.__FILE_NAME, "a") as file:
            file.write(table_row)

    @classmethod
    def update_book(cls, updated_book):
        old_books = cls.get_all_books()
        new_books = [updated_book if updated_book.title == old_book.title else old_book for old_book in old_books]

        cls.initialise(new_books)

    @classmethod
    def delete_book(cls, book):
        old_books = cls.get_all_books()
        new_books = list(filter(lambda b: b.title != book.title, old_books))

        cls.initialise(new_books)
