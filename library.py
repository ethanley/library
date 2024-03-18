from sys import argv
from sub.options import Option, Options
from sub.database import Database
from sub.book import Book

def show_help():
    print("Help!")

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
        Option("h", "help", show_help),
        Option("v", "version", show_version),
        Option("l", "list", list_all_books),
        Option("a", "with-author", list_books_with_author, True),
        Option("n", "new", add_new_book),
        Option("r", "read-only", lambda: list_by_read_status(True)),
        Option("u", "unread_only", lambda: list_by_read_status(False)),
        Option("f", "finished", mark_as_finished, True),
        Option("d", "delete", delete_book, True)
    ]

def main():
    chosen_option, parameter = Options(ALL_POSSIBLE_OPTIONS).get_option(argv)

    if (chosen_option.has_parameter):
        chosen_option.action(parameter)
    else:
        chosen_option.action()

if __name__ == "__main__":
    main()
