class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        self.books.append(Book(title, author))
        print("Book Added Successfully!\n")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available.\n")
            return

        print("\nLibrary Books")
        print("-" * 30)
        for i, book in enumerate(self.books, start=1):
            print(f"\nBook {i}")
            book.display()
        print()

    def issue_book(self):
        title = input("Enter Book Title to Issue: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book Issued Successfully!\n")
                else:
                    print("Book Already Issued!\n")
                return

        print("Book Not Found!\n")

    def return_book(self):
        title = input("Enter Book Title to Return: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book Returned Successfully!\n")
                else:
                    print("This Book Was Not Issued!\n")
                return

        print("Book Not Found!\n")


library = Library()

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")
