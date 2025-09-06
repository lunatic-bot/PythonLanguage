from abc import ABC, abstractmethod

## Abstraction
class LibraryMember(ABC):
    # --- Abstract method (rule) ---
    @abstractmethod
    def get_role(self):
        pass

     # --- Concrete method (ready-made) ---
    def greet(self):
        return f"Hello, I am {self.name}, and I am a {self.get_role()}."



class Book:
    def __init__(self, title, author, isbn):
        if not title.strip():
            raise ValueError("Title can not be empty.")
        if not author.strip():
            raise ValueError("Author can not be empty.")
        if not (isbn.isdigit() and len(isbn) == 5):
            raise ValueError("ISBN mush be a 5-digit number.")
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True  ## Protected attibute

    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False
    
    def return_book(self):
        # if not self._available:
        #     self._available = True
        #     return True
        # return False
        self._available = True
        return True
        
    def __str__(self):
        return f"{self.title} by {self.author} ({'Available' if self._available else 'Borrowed'})"

    


## inheritance and polymorphism
class User(LibraryMember):
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Member Name can not be empty.")
        self.name = name

    def get_role(self):
        return "User"
    
class Student(User):
    def get_role(self):
        return "Student"
    
class Librarian(User):
    def get_role(self):
        return "Librarian"
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No Books in library.")
        else:
            for book in self.books:
                print(book)

    def __len__(self):   ## operator overloading
        """Return total number of books in library"""
        return len(self.books)
    
    def __contains__(self, title):  ## operator overloading
        """Check if a book with given title exists"""
        return any(book.title == title for book in self.books)
    
    # --- Static method ---
    @staticmethod
    def is_isbn_valid(isbn):
        """Simple validation: must be 5-digit number"""
        return len(isbn) == 5 ## simple check

    # --- Class method ---
    @classmethod
    def from_booklist(cls, book_list):
        """Alternative constructor: create Library from list of Book objects"""
        lib = cls() # create new Library object
        for b in book_list:
            lib.add_book(b)
        return lib

    
        


if __name__ == "__main__":

    ## class and static menthods
    # print("\n--- Static Method Test ---")
    # print("Valid ISBN (12345)?", Library.is_isbn_valid("12345"))   # True
    # print("Valid ISBN (12AB5)?", Library.is_isbn_valid("12AB5"))   # False
    # print("Valid ISBN (123)?", Library.is_isbn_valid("123"))       # False

    ## class method test
    books = [
            Book("OOP in Python", "Smith", "12345"),
            Book("Data Science", "Jones", "54321")
    ]
    lib2 = Library.from_booklist(books) ## calls like lib2 = Library.from_booklist(Library, books) internally
    lib2.show_books()
    print("Total books in lib2:", len(lib2))

    #########################################################################

    # library = Library()
    # b1 = Book("Programming in C", "Denis Ritchie", "98752")
    # b2 = Book("Programming in Java", "Java Founder", "87352")
    # b3 = Book("Python Basics", "Guido", "54321")

    # library.add_book(b1)
    # library.add_book(b2)
    # library.add_book(b3)

    # print('\nBooks in library : ')
    # library.show_books()

    # b1.borrow()
    # library.show_books()

    # ## magic menthods - 
    # print("\nTotal books:", len(library))          # uses __len__
    # print("Is '1984' in library?", "1984" in library)   # uses __contains__
    # print("Is 'Harry Potter' in library?", "Harry Potter" in library)

    # print(library)

    # empty_lib = Library()
    # print(len(empty_lib))         # 0
    # print("1984" in empty_lib)    # False
    # empty_lib.show_books()  



    # lib = Library()
    # lib.add_book(Book("1984", "George Orwell", "12345"))
    # lib.add_book(Book("1984", "Fake Author", "67890"))
    # print("1984" in lib)


    ############################################################################

    # s1 = Student("Alice")
    # l1 = Librarian("Bob")
    # u1 = User("Charlie")

    # print(f"{s1.name} is a {s1.get_role()}")
    # print(f"{l1.name} is a {l1.get_role()}")   # Bob is a Librarian
    # print(f"{u1.name} is a {u1.get_role()}")   # Charlie is a User


    # # m = LibraryMember() # You can’t create an object of an abstract class — this enforces abstraction.

    # members = [Student("Alice"), Librarian("Bob"), User("Charlie")]
    # for m in members:
    #     print(m.get_role()) # same method name, different behaviors. - polymorphic

    # # m = User("")
    # # print(m.get_role())



    ####################################################################    

    # book1 = Book("Programming in C", "Denis Ritchie", "98752")
    # book2 = Book("Programming in Java", "Java Founder", "87352")
    # book3 = Book("Python Basics", "Guido", "54321")
    # book4 = Book("Clean Code", "Robert Martin", "11111")
    # book5 = Book("Some", "Author", "75321")

    # print(book1.author)
    # print(book2.__str__)
    # print(book1.borrow())
    # print(book1)
    # print(book1.borrow())
    # print(book1.return_book())
    # print(book1)

    # print(book1, book2, book3, book4, sep='\n')
    # book1.borrow()
    # print(book1, book2, book3, book4, sep='\n')
    # print(book5)

    # print(book1.borrow())   # True
    # print(book1.borrow())   # False
    # print(book1.return_book())
    # print(book1.return_book()) 

