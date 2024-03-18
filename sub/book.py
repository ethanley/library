class Book:
    def __init__(self, title, author, times_read=0):
        self.title = title
        self.author = author
        self.times_read = times_read

    def mark_as_read(self):
        self.times_read += 1

    def to_string(self):
        return "%s\n |-by %s\n |- read %s time(s)" % (self.title, self.author, self.times_read)

    def map_to_table_row(self):
        return "%s,%s,%s" % (self.title, self.author, self.times_read)

    @staticmethod
    def map_table_row_to_book(table_row):
        title, author, times_read = table_row.split(',')
        book = Book(title, author, int(times_read))
        return book

    @staticmethod
    def filter_by_author(books, author):
        return list(filter(lambda b: b.author == author, books))

    @staticmethod
    def filter_by_read(books, read):
        return list(filter(lambda b: (b.times_read > 0) == read, books))

    @staticmethod
    def get_book_with_title(books, title):
        matches = list(filter(lambda b: b.title == title, books))

        if (len(matches) != 1):
            return None

        return matches[0]
