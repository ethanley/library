from sys import argv
from util.options import Option, Options

def help():
    print("Help!")
def list():
    raise NotImplementedError()

ALL_POSSIBLE_OPTIONS = [
        Option("h", "help", help)
    ]

# SHORT_OPTIONS = "hvla:runf:"
# LONG_OPTIONS = [
#         "help",
#         "version",
#         "list",
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
