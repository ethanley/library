from sys import argv
from sub.options import Option, Options, IncorrectUsageError
from sub.database import Database
from sub.book import Book

ALL_POSSIBLE_OPTIONS = None

HELP_MESSAGE = lambda: """Usage: library.py [OPTIONS...]

Catalogue books and record the number of times they've been read

""" + '\n'.join([option.to_string() for option in ALL_POSSIBLE_OPTIONS]) + """
\nPlease report bugs to <https://github.com/ethanley/library/issues>"""

def show_help():
    print(HELP_MESSAGE())

def show_incorrect_usage():
    print("Incorrect usage")
    show_help()

def show_version():
    print("library.py version 0.1")

def print_books(books):
    formatted_titles = '\n'.join([book.title for book in books])
    print(formatted_titles)

def list_all_books():
    books = Database.get_all_books()
    print_books(books)

def list_books_with_author(author):
    all_books = Database.get_all_books()
    books_by_author = Book.filter_by_author(all_books, author)
    print_books(books_by_author)

def list_by_read_status(has_been_read):
    all_books = Database.get_all_books()
    filtered_books = Book.filter_by_read(all_books, has_been_read)
    print_books(filtered_books)

def print_book(title):
    all_books = Database.get_all_books()
    book = Book.get_book_with_title(all_books, title)
    if (book == None):
        print(f"No book found matching title: `{title}`")
        return
    print(book.to_string())

def add_new_book():
    title = input("Title:\t\t")
    author = input("Author:\t\t")
    times_read = input("Times Read:\t")
    times_read = int(times_read) if times_read.isdigit() else None

    book = Book(title, author, int(times_read))
    Database.add_book(book)

def mark_as_finished(title):
    all_books = Database.get_all_books()
    book = Book.get_book_with_title(all_books, title)
    if (book == None):
        print(f"No book found matching title: `{title}`")
        return
    book.mark_as_read()
    Database.update_book(book)

def delete_book(title):
    all_books = Database.get_all_books()
    book = Book.get_book_with_title(all_books, title)
    if (book == None):
        print(f"No book found matching title: `{title}`")
        return
    Database.delete_book(book)

ALL_POSSIBLE_OPTIONS = [
        Option("h", "help", show_help, "Display this help message"),
        Option("v", "version", show_version, "Show program version"),
        Option("l", "list", list_all_books, "List all books"),
        Option("a", "with-author", list_books_with_author, "List all books with author", "AUTHOR"),
        Option("i", "info", print_book, "Display information about a book", "TITLE"),
        Option("n", "new", add_new_book, "Add a new book"),
        Option("r", "read-only", lambda: list_by_read_status(True), "List all read books"),
        Option("u", "unread_only", lambda: list_by_read_status(False), "List all unread books"),
        Option("f", "finished", mark_as_finished, "Mark a book as read", "TITLE"),
        Option("d", "delete", delete_book, "Delete a book", "TITLE")
    ]

def main():
    try:
        chosen_option, parameter = Options(ALL_POSSIBLE_OPTIONS).get_option(argv)
    except IncorrectUsageError:
        show_incorrect_usage()
    except Exception as err:
        print(err)
    else:
        if (chosen_option.has_parameter()):
            chosen_option.action(parameter)
        else:
            chosen_option.action()

if __name__ == "__main__":
    main()
