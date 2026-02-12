from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self._password = "default_pass"  # Consider making this private + hashed in real code

    @abstractmethod
    def get_role(self):
        pass

    def display_info(self):
        return f"Username: {self._username}, Email: {self._email}"

class Seller(User):
    def __init__(self, username, email, seller_id):
        super().__init__(username, email)
        self.seller_id = seller_id

    def get_role(self):
        return "Seller"

    def display_info(self):
        return f"{super().display_info()}, ID: {self.seller_id} (Seller)"


class Buyer(User):
    def __init__(self, username, email, buyer_id):
        super().__init__(username, email)
        self.buyer_id = buyer_id

    def get_role(self):
        return "Buyer"          # ← fixed: missing space after return

    # Optional: you can override display_info if you want buyer-specific output
    # def display_info(self):
    #     return f"{super().display_info()}, ID: {self.buyer_id} (Buyer)"


class Book:
    def __init__(self, title, price, condition):
        self.title = title
        self.price = price
        self.condition = condition
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Sold"
        return f"Title: {self.title}, Price: ${self.price:.2f}, Condition: {self.condition}, Status: {status}"


class Order:
    def __init__(self, buyer, book):
        if not isinstance(buyer, Buyer):
            raise TypeError("buyer must be a Buyer instance")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        if not book.available:
            raise ValueError("This book is not available")

        self.buyer = buyer
        self.book = book
        self.status = "Pending"

    def confirm(self):
        self.status = "Confirmed"
        self.book.available = False

    def display_info(self):
        return (f"Order - Buyer: {self.buyer._username}, "
                f"Book: {self.book.title}, "
                f"Status: {self.status}")
