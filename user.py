class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"[{self.user_id}] {self.name} (Borrowed: {len(self.borrowed_books)})"