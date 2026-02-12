from collections import deque
from models import Seller, Buyer, Book, Order

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TransactionHistory:
    def __init__(self):
        self.head = None

    def add(self, transaction):
        new_node = Node(transaction)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        history = []
        while current:
            history.append(current.data)
            current = current.next
        return history

class Marketplace:
    def __init__(self):
        self.books = []             # available + sold books
        self.pending_orders = deque()  # (buyer, book) tuples
        self.history = TransactionHistory()

    def add_book(self, book):
        if not isinstance(book, Book):
            return "Error: Invalid book object"
        self.books.append(book)
        return f"Book added successfully: {book.display_info()}"

    def place_order(self, buyer, book):
        if not isinstance(buyer, Buyer):
            return "Error: Invalid buyer"
        if not isinstance(book, Book):
            return "Error: Invalid book"

        try:
            order = Order(buyer, book)   # this checks availability
            order.confirm()              # marks as Confirmed + sets book unavailable
            self.history.add(
                f"Confirmed order → {buyer._username} bought '{book.title}' for ${book.price}"
            )
            return f"Order confirmed!\n{order.display_info()}"
        except ValueError as e:
            # Book not available → add to waitlist
            self.pending_orders.append((buyer, book))
            return f"{str(e)}. Added to waitlist (position {len(self.pending_orders)})."
        except TypeError as e:
            return f"Error: {e}"

    def cancel_order(self):
        if not self.pending_orders:
            return "No pending orders in the waitlist."
        
        buyer, book = self.pending_orders.popleft()
        return (f"Cancelled oldest waitlist order: "
                f"{buyer.display_info()} → '{book.title}'")

    def view_listings(self):
        if not any(book.available for book in self.books):
            return "No books available for sale at the moment."
        return "\n".join(book.display_info() for book in self.books if book.available)

    def recommend_with_radix(self):
        """Simple radix sort demo on book prices + placeholder graph recommendation"""
        if not self.books:
            return "No books in the system yet."

        def radix_sort_prices(book_list):
            if not book_list:
                return []
            # Extract prices
            prices = [b.price for b in book_list]
            max_val = max(prices) if prices else 0
            exp = 1
            while max_val // exp > 0:
                buckets = [[] for _ in range(10)]
                for book in book_list:
                    digit = (book.price // exp) % 10
                    buckets[digit].append(book)
                book_list = [b for bucket in buckets for b in bucket]
                exp *= 10
            return book_list

        # Sort only available books by price (ascending)
        available_books = [b for b in self.books if b.available]
        sorted_books = radix_sort_prices(available_books)

        if not sorted_books:
            return "No available books to recommend."

        lines = ["Price-sorted recommendations (cheapest first):"]
        for book in sorted_books:
            lines.append(f"  ${book.price:5.2f}  {book.title}  ({book.condition})")

        # Very simple placeholder for graph-based rec (can be expanded later)
        lines.append("\nGraph-based similar books: (placeholder)")
        lines.append("  • If you like 'Python Programming' → try 'Clean Code'")

        return "\n".join(lines)
