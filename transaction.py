import datetime

class Transaction:
    def __init__(self, transaction_type, user_id, book_id):
        self.transaction_type = transaction_type  # 'issue' or 'return'
        self.user_id = user_id
        self.book_id = book_id
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.title()} - Book: {self.book_id}, User: {self.user_id}"