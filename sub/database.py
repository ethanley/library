import os.path
from sub.book import Book

class Database:
    __FILE_NAME = "./database/books.csv"

    @classmethod
    def filepath(cls):
        # TODO make absolute
        return cls.__FILE_NAME

    @classmethod
    def is_initialised(cls):
        return os.path.isfile(cls.__FILE_NAME)

    @classmethod
    def initialise(cls):
        open(cls.__FILE_NAME, "x")

    @classmethod
    def get_all_books(cls):
        if (not cls.is_initialised()):
            cls.initialise()

        with open(cls.__FILE_NAME, "r") as file:
            data = file.read()

        rows = data.split('\n')
        table = [row.split(',') for row in rows if row != '']

        books = [Book(*row) for row in table]

        return books
