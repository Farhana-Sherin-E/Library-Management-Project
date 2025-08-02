from library import Library
from book import Book
from user import User

def sample_data(library):
    # Add sample books
    library.add_book(Book("B1", "The Alchemist", "Paulo Coelho", 1988))
    library.add_book(Book("B2", "Atomic Habits", "James Clear", 2018))
    library.add_book(Book("B3", "Clean Code", "Robert C. Martin", 2008))
    # Add sample users
    library.register_user(User("U1", "Alice"))
    library.register_user(User("U2", "Bob"))
    library.register_user(User("U3", "Charlie"))

def print_menu():
    print("\n==== Library Management System ====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. List Books")
    print("4. Search Book by Title")
    print("5. Search Book by Author")
    print("6. Register User")
    print("7. Search User by Name")
    print("8. Issue Book")
    print("9. Return Book")
    print("10. Show User's Borrowed Books")
    print("11. Show Book's Waiting List")
    print("12. Show Recent Transactions")
    print("0. Exit")
    print("===================================")

def main():
    library = Library()
    sample_data(library)
    while True:
        print_menu()
        choice = input("Enter option: ")
        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            library.add_book(Book(book_id, title, author, year))
        elif choice == "2":
            book_id = input("Book ID to remove: ")
            library.remove_book(book_id)
        elif choice == "3":
            sort_by = input("Sort by (title/author/year): ")
            books = library.list_books(sort_by)
            for book in books:
                print(book)
        elif choice == "4":
            title = input("Enter title to search: ")
            results = library.search_books_by_title(title)
            for book in results:
                print(book)
        elif choice == "5":
            author = input("Enter author to search: ")
            results = library.search_books_by_author(author)
            for book in results:
                print(book)
        elif choice == "6":
            user_id = input("User ID: ")
            name = input("Name: ")
            library.register_user(User(user_id, name))
        elif choice == "7":
            name = input("Enter name to search: ")
            results = library.search_users_by_name(name)
            for user in results:
                print(user)
        elif choice == "8":
            user_id = input("User ID: ")
            book_id = input("Book ID: ")
            library.issue_book(user_id, book_id)
        elif choice == "9":
            user_id = input("User ID: ")
            book_id = input("Book ID: ")
            library.return_book(user_id, book_id)
        elif choice == "10":
            user_id = input("User ID: ")
            library.show_user_borrowed_books(user_id)
        elif choice == "11":
            book_id = input("Book ID: ")
            library.show_book_waiting_list(book_id)
        elif choice == "12":
            n = int(input("Show how many recent transactions? "))
            library.show_transactions(n)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()