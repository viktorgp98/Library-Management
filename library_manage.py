import sys
from Book import Book

class Library:
    def __init__(self):
        """
            Inicia la lista de libros de la libreria
        """
        self.books = []

    def add_book(self):
        """
        Agrega un nuevo libro a la lista de libros
        """
        newBook=input("Enter the title of the book:")
        book=Book(newBook)
        self.books.append(book)
        print(f"'{newBook}' has been added to the library.")


    def borrow_book(self):
        title = input(f"Enter the title of the book to borrow:")
        for book in self.books:
            if book.title == title and book.is_available:
                print(book.mark_as_borrowed())


    def return_book(self):
        title = input(f"Enter the title of the book to return:")
        for book in self.books:
            if book.title == title and not book.is_available:
                print( book.mark_as_returned())
    def view_books(self):
        """
        Muestra un listado de los libros disponibles1
        """
        available_books = [f"- {book.title}" for book in self.books if book.is_available] 
        if available_books:
            print( "Available books: \n" + "\n".join(available_books)) 
        else:
            print( "No books available right now.")

    def run(self):
        while(True):
            print("\n1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Available Books\n5. Exit")
            choice = input("Enter choice:")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.view_books()
            elif choice == '5':
                print ("Goodbye!")
                sys.exit()                   

if __name__ == "__main__":
    library = Library()
    library.run()



