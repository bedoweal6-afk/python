class book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_available=True
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Available: {self.available}")
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn


class member:
    def __init__(self,name,members_id):
        self.name=name
        self.members_id=members_id
        self.borrowed_books=[]
    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self,book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

class staffmember(member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.append(book)
        print(f"{self.name} added {book.title} to the library")
        library.append(book1)
staff=staffmember("alice","2001","51001")
book1=book("1984","George Orwell","1234567890")
book2 = book("OOP Concepts", "Sara Youssef", "987654321")

library =[]
staff = staffmember("Mostafa", "M001", "S001")
staff.add_book(library, book1)
staff.add_book(library, book2)

member = member("Laila", "M002")
member.borrow_book(book1)
member.return_book(book1)
member.borrow_book(book1)
member.borrow_book(book2)
print(f"Borrowed books: {[book1.title for book1 in member.borrowed_books]}")