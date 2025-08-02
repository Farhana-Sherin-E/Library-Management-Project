from collections import deque
from book import Book
from user import User
from transaction import Transaction

class Library:
    def __init__(self):
        self.books = {}         # book_id: Book
        self.users = {}         # user_id: User
        self.transactions = []  # Stack of Transaction objects
        self.waiting_list = {}  # book_id: deque of user_ids

    # Book Management
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book.book_id] = book
            print("Book added successfully.")

    def remove_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id].is_issued:
                print("Cannot remove book. Book is currently issued.")
            else:
                del self.books[book_id]
                print("Book removed.")
        else:
            print("Book not found.")

    def search_books_by_title(self, title):
        result = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                result.append(book)
        return result

    def search_books_by_author(self, author):
        result = []
        for book in self.books.values():
            if author.lower() in book.author.lower():
                result.append(book)
        return result

    def list_books(self, sort_by="title"):
        if sort_by == "title":
            return sorted(self.books.values(), key=lambda b: b.title)
        elif sort_by == "author":
            return sorted(self.books.values(), key=lambda b: b.author)
        elif sort_by == "year":
            return sorted(self.books.values(), key=lambda b: b.year)
        else:
            return list(self.books.values())

    # User Management
    def register_user(self, user):
        if user.user_id in self.users:
            print("User ID already exists.")
        else:
            self.users[user.user_id] = user
            print("User registered successfully.")

    def search_users_by_name(self, name):
        result = []
        for user in self.users.values():
            if name.lower() in user.name.lower():
                result.append(user)
        return result

    # Transactions
    def issue_book(self, user_id, book_id):
        if book_id not in self.books:
            print("Book not found.")
            return
        if user_id not in self.users:
            print("User not found.")
            return
        book = self.books[book_id]
        user = self.users[user_id]

        if book.is_issued:
            # Add to waiting list
            if book_id not in self.waiting_list:
                self.waiting_list[book_id] = deque()
            if user_id not in self.waiting_list[book_id]:
                self.waiting_list[book_id].append(user_id)
                print("Book is issued. Added to waiting list.")
            else:
                print("Already in waiting list.")
            return

        book.is_issued = True
        book.issued_to = user_id
        user.borrowed_books.append(book_id)
        self.transactions.append(Transaction("issue", user_id, book_id))
        print("Book issued successfully.")

    def return_book(self, user_id, book_id):
        if book_id not in self.books or user_id not in self.users:
            print("Book/User not found.")
            return
        book = self.books[book_id]
        user = self.users[user_id]
        if book_id not in user.borrowed_books:
            print("This user did not borrow this book.")
            return
        book.is_issued = False
        book.issued_to = None
        user.borrowed_books.remove(book_id)
        self.transactions.append(Transaction("return", user_id, book_id))
        print("Book returned successfully.")

        # Issue to next in waiting list if any
        if book_id in self.waiting_list and self.waiting_list[book_id]:
            next_user_id = self.waiting_list[book_id].popleft()
            print(f"Issuing book to next user in waiting list: {next_user_id}")
            self.issue_book(next_user_id, book_id)

    def show_transactions(self, last_n=5):
        print("Recent Transactions:")
        for trans in self.transactions[-last_n:][::-1]:
            print(trans)

    def show_user_borrowed_books(self, user_id):
        if user_id not in self.users:
            print("User not found.")
            return
        user = self.users[user_id]
        print(f"Books borrowed by {user.name}:")
        for book_id in user.borrowed_books:
            print(self.books[book_id])

    def show_book_waiting_list(self, book_id):
        if book_id in self.waiting_list:
            print(f"Waiting list for book {book_id}: {list(self.waiting_list[book_id])}")
        else:
            print("No waiting list for this book.")