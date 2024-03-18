# library.py
Catalogue books and record the number of times they've been read.

This is a quick project, built as teaching material whilst demonstrating some cool Python stuff.

## Setup
```sh
$ python setup.py
```

Run the file `setup.py` to initialise the database and populate it with some example data.

## Usage
```sh
$ python library.py [OPTIONS]
```

Run the file `library.py` with the command line arguments applicable to your use case.

### Options

`-h` / `--help`
: Display a help message.

`-v` / `--version`
: Show program version.

`-l` / `--list`
: List all books by title.

`-a [AUTHOR]` / `--with-author [AUTHOR]`
: List all books authored by the specified `[AUTHOR]`. Remember to format the author's name as a string if it contains spaces.

`-n` / `--new`
: Add a new book. The program will take user input for the book's title and author, as well as how many times you've read it.

`-r` / `--read-only`
: Lists all books which have been read at least once.

`-u` / `--unread-only`
: Lists only those books which haven't been read.

`-f [TITLE]` / `--finished [TITLE]`
: Marks the book with the specified `[TITLE]` as read.

`-d [TITLE]` / `--delete [TITLE]`
: Deletes the book with the specified `[TITLE]` from the database.

## Issues
Please report bugs to [https://github.com/ethanley/library/issues](https://github.com/ethanley/library/issues).
