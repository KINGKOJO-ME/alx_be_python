class Book:
    # A class representing a book in the library.

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        # Mark the book as checked out.
        self .is_checked_out = True

    def return_book(self):
        # Mark the book as returned.
        self.is_checked_out = False

class Library:
    # A class representing a library that manages books.
    def __init__(self):
        self._books = []

    def add_book(self, book):
        # Add a book to the library.
        self.books.append(book)

    def check_out_book(self, title):
        # check out a book by title. Returns True if successful.
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        # return a book by title. Returns True if successful.
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        # list all available (not checked out) books.
        for book in self._books:
            if book.is_available():
                print(f'"{book.title} by {book.author}')
                