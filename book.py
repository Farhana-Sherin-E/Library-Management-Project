class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_issued = False
        self.issued_to = None

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} ({self.year}) - {status}"