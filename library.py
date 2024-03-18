from sys import argv
from sub.options import Option, Options
from sub.database import Database
from sub.book import Book

def show_help():
    print("Help!")

def show_version():
    print("library.py version 0.1")

def list_all_books():
    books = Database.get_all_books()
    print(books)

def list_books_with_author(author):
	books = Book.filter_by_author(Database.get_all_books(), author)
	print(books)

def add_new_book():
	raise NotImplementedError()

ALL_POSSIBLE_OPTIONS = [
        Option("h", "help", show_help),
        Option("v", "version", show_version),
        Option("l", "list", list_all_books),
		Option("a", "with-author", list_books_with_author, True),
		Option("n", "new", add_new_book)
    ]

# SHORT_OPTIONS = "hvla:runf:"
# LONG_OPTIONS = [
#         "help",
#         "version",
#         "list-all",
#         "author=",
#         "read-only",
#         "unread-only",
#         "new",
#         "finished="
#     ]

def main():
    chosen_option, parameter = Options(ALL_POSSIBLE_OPTIONS).get_option(argv)

    if (chosen_option.has_parameter):
        chosen_option.action(parameter)
    else:
        chosen_option.action()

if __name__ == "__main__":
    main()
