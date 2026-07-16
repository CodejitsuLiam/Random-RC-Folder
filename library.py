class Book:
    def __init__(self, title: str, author: str, copies: int = 2):
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def checkout(self) -> bool:
        if self.available_copies <= 0:
            return False
        self.available_copies -= 1
        return True

    def return_copy(self) -> None:
        if self.available_copies < self.total_copies:
            self.available_copies += 1

    def __repr__(self) -> str:
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"


class Patron:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_titles = set()

    def has_borrowed(self, title: str) -> bool:
        return title in self.borrowed_titles

    def borrow(self, title: str) -> bool:
        if self.has_borrowed(title):
            return False
        self.borrowed_titles.add(title)
        return True

    def return_book(self, title: str) -> bool:
        if not self.has_borrowed(title):
            return False
        self.borrowed_titles.remove(title)
        return True

    def __repr__(self) -> str:
        borrowed = ", ".join(sorted(self.borrowed_titles)) or "none"
        return f"{self.name} has borrowed: {borrowed}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book) -> None:
        if book.title in self.books:
            existing = self.books[book.title]
            existing.total_copies += book.total_copies
            existing.available_copies += book.available_copies
        else:
            self.books[book.title] = book

    def checkout_book(self, title: str, patron: Patron) -> bool:
        if title not in self.books:
            return False
        book = self.books[title]
        if not book.available_copies:
            return False
        if not patron.borrow(title):
            return False
        return book.checkout()

    def return_book(self, title: str, patron: Patron) -> bool:
        if title not in self.books:
            return False
        if not patron.return_book(title):
            return False
        self.books[title].return_copy()
        return True

    def list_books(self) -> None:
        print("Library inventory:")
        for book in sorted(self.books.values(), key=lambda item: item.title):
            print(f"- {book}")

    def show_book_status(self, title: str) -> None:
        if title not in self.books:
            print(f"{title} is not in the library.")
            return
        print(self.books[title])


if __name__ == "__main__":
    library = Library()
    initial_books = [
        Book("1984", "George Orwell", copies=2),
        Book("To Kill a Mockingbird", "Harper Lee", copies=2),
        Book("The Hobbit", "J.R.R. Tolkien", copies=2),
        Book("Pride and Prejudice", "Jane Austen", copies=2),
        Book("The Great Gatsby", "F. Scott Fitzgerald", copies=2),
        Book("Moby Dick", "Herman Melville", copies=2),
        Book("Dune", "Frank Herbert", copies=2),
        Book("Brave New World", "Aldous Huxley", copies=2),
        Book("The Catcher in the Rye", "J.D. Salinger", copies=2),
        Book("The Chronicles of Narnia", "C.S. Lewis", copies=2),
    ]
    for book in initial_books:
        library.add_book(book)

    patron_name = input("Enter your name: ").strip() or "Guest"
    patron = Patron(patron_name)

    print(f"\nWelcome, {patron.name}!")

    while True:
        print("\nChoose an option:")
        print("1. Check out a book")
        print("2. Return a book")
        print("3. Donate a book")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter the book title to check out: ").strip()
            if library.checkout_book(title, patron):
                print(f"{patron.name} checked out {title}")
                library.show_book_status(title)
            else:
                print(f"{patron.name} could not check out {title}")
        elif choice == "2":
            title = input("Enter the book title to return: ").strip()
            if library.return_book(title, patron):
                print(f"{patron.name} returned {title}")
                library.show_book_status(title)
            else:
                print(f"{patron.name} could not return {title}")
        elif choice == "3":
            title = input("Enter the book title to donate: ").strip()
            author = input("Enter the author's name: ").strip() or "Unknown Author"
            if title:
                library.add_book(Book(title, author, copies=1))
                print(f"Thank you for donating {title} by {author}!")
                library.show_book_status(title)
            else:
                print("Please enter a title.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
