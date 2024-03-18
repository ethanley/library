from sub.database import Database
from sub.book import Book

default_books = [
        Book("Zen and the Art of Motorcycle Maintenance", "Robert M. Pirsig", 1),
        Book("Speaker for the Dead", "Orson Scott Card", 2),
        Book("Lila", "Robert M. Pirsig", 0),
        Book("The Farthest Shore", "Ursula K. Le Guin", 1),
        Book("Gilead", "Marilynne Robinson", 1),
        Book("Orlando", "Virginia Woolf", 0)
]

def __main__():
    Database.initialise(default_books)

if (__name__ == "__main__"):
    __main__()
