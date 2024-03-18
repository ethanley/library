from sys import argv
from util.options import Option, Options
from util.database import Database

def show_help():
    print("Help!")

def show_version():
    print("library.py version 0.1")

def list_all_books():
    books = Database.get_all_books()
    print(books)

ALL_POSSIBLE_OPTIONS = [
        Option("h", "help", show_help),
        Option("v", "version", show_version),
        Option("l", "list", list_all_books)
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
