class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_info(self, title=None, author=None, genre=None, quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if quantity is not None:
            self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Quantity: {self.quantity}"


class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id

    def update_info(self, name=None, contact=None):
        if name:
            self.name = name
        if contact:
            self.contact = contact

    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact}, Membership ID: {self.membership_id}"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def add_borrower(self, borrower):
        self.borrowers[borrower.membership_id] = borrower

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]

    def borrow_book(self, isbn, membership_id, due_date):
        if isbn in self.books and membership_id in self.borrowers:
            book = self.books[isbn]
            if book.quantity > 0:
                book.quantity -= 1
                self.borrowed_books[membership_id] = {"isbn": isbn, "due_date": due_date}
                return True
            else:
                print("Book not available.")
                return False
        else:
            print("Invalid ISBN or Membership ID.")
            return False

    def return_book(self, membership_id):
        if membership_id in self.borrowed_books:
            isbn = self.borrowed_books[membership_id]["isbn"]
            if isbn in self.books:
                self.books[isbn].quantity += 1
            del self.borrowed_books[membership_id]

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results

    def show_availability(self, isbn):
        if isbn in self.books:
            return self.books[isbn].quantity
        else:
            return 0


# Example usage
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789", "Fiction", 5)
    book2 = Book("1984", "George Orwell", "987654321", "Dystopian", 3)
    library.add_book(book1)
    library.add_book(book2)

    # Add borrowers
    borrower1 = Borrower("Alice Smith", "alice@example.com", "001")
    borrower2 = Borrower("Bob Johnson", "bob@example.com", "002")
    library.add_borrower(borrower1)
    library.add_borrower(borrower2)

    # Borrow a book
    library.borrow_book("123456789", "001", "2024-07-01")

    # Return a book
    library.return_book("001")

    # Search for books
    search_results = library.search_books(author="George Orwell")
    for book in search_results:
        print(book)

    # Show book availability
    print("Availability of '1984':", library.show_availability("987654321"))
