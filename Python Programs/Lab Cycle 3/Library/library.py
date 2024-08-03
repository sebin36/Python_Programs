# Create a class Library
class Library:
    # Initializing an empty list shelf.
    def __init__(self,shelf):
        self.shelf = shelf

    def add_book(self,book_title):
        self.shelf.append(book_title)
        print('Book has been added')

    def remove_book(self,book_title):
        self.shelf.remove(book_title)
        print('The Book has been removed.')

    def list_books(self):
        print('Books in Library:')
        return self.shelf

    
