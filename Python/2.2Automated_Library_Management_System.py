from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.catalog = {
            "001": {"title": "Book 1", "author": "Author 1", "quantity": 5},
            "002": {"title": "Book 2", "author": "Author 2", "quantity": 3},
            "003": {"title": "Book 3", "author": "Author 3", "quantity": 2},
        }
        self.users = {}
        self.transactions = []

    def display_catalog(self):
        print("Catalog:")
        for book_id, book_info in self.catalog.items():
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")

    def register_user(self, user_id, name):
        self.users[user_id] = {"name": name, "books_checked_out": []}

    def checkout_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.catalog:
            print("Book not found.")
            return
        if len(self.users[user_id]["books_checked_out"]) >= 3:
            print("User has reached the maximum limit of checked out books.")
            return
        if self.catalog[book_id]["quantity"] <= 0:
            print("Book not available.")
            return

        self.catalog[book_id]["quantity"] -= 1
        checkout_date = datetime.now()
        self.users[user_id]["books_checked_out"].append({"book_id": book_id, "checkout_date": checkout_date})
        self.transactions.append({"user_id": user_id, "book_id": book_id, "action": "checkout", "date": checkout_date})

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.catalog:
            print("Book not found.")
            return

        for book in self.users[user_id]["books_checked_out"]:
            if book["book_id"] == book_id:
                self.catalog[book_id]["quantity"] += 1
                self.users[user_id]["books_checked_out"].remove(book)
                return_date = datetime.now()
                checkout_date = book["checkout_date"]
                days_overdue = (return_date - checkout_date).days - 14
                if days_overdue > 0:
                    fine = days_overdue * 1
                    print(f"Book returned {days_overdue} days overdue. Fine: ${fine}")
                else:
                    print("Book returned on time.")
                self.transactions.append({"user_id": user_id, "book_id": book_id, "action": "return", "date": return_date})
                return
        print("Book not checked out by this user.")

    def list_overdue_books(self, user_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        overdue_books = []
        total_fine = 0
        for transaction in self.transactions:
            if transaction["user_id"] == user_id and transaction["action"] == "return":
                book_id = transaction["book_id"]
                checkout_date = None
                for book in self.users[user_id]["books_checked_out"]:
                    if book["book_id"] == book_id:
                        checkout_date = book["checkout_date"]
                        break
                if checkout_date is not None:
                    return_date = transaction["date"]
                    days_overdue = (return_date - checkout_date).days - 14
                    if days_overdue > 0:
                        fine = days_overdue * 1
                        total_fine += fine
                        overdue_books.append((book_id, fine))
        if overdue_books:
            print("Overdue Books:")
            for book_id, fine in overdue_books:
                print(f"Book ID: {book_id}, Fine: ${fine}")
            print(f"Total Fine Due: ${total_fine}")
        else:
            print("No overdue books.")

# Interactive user interface
library = Library()

while True:
    print("\n1. Display Catalog")
    print("2. Register User")
    print("3. Checkout Book")
    print("4. Return Book")
    print("5. List Overdue Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_catalog()
    elif choice == "2":
        user_id = input("Enter User ID: ")
        name = input("Enter User Name: ")
        library.register_user(user_id, name)
        print("User registered successfully.")
    elif choice == "3":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID to Checkout: ")
        library.checkout_book(user_id, book_id)
    elif choice == "4":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID to Return: ")
        library.return_book(user_id, book_id)
    elif choice == "5":
        user_id = input("Enter User ID: ")
        library.list_overdue_books(user_id)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
