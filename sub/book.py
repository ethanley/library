class Book:
    def __init__(self, title, author, times_read=0):
        self.title = title
        self.author = author
        self.times_read = int(times_read)

    def read(self):
        self.times_read += 1

    @staticmethod
    def filter_by_author(books, author):
        return list(filter(lambda b: b.author == author, books))
