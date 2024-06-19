# Library Management System

This is a simplified library management system implemented in Python using Object-Oriented Programming (OOP) concepts.

## Features
- **Book Management**: Add, update, remove books.
- **Borrower Management**: Add, update, remove borrowers.
- **Book Borrowing and Returning**: Borrow and return books.
- **Book Search and Availability**: Search for books and check availability.

## Usage
```python
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
