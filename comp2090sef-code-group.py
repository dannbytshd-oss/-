"""
Campus Second-hand Book Trading Platform (COMP 2090SEF Group Assignment)
Integrated single-file implementation with core concepts: OOP (Encapsulation/Inheritance/Abstraction), 
Linked List, Linear/Binary Search, Selection/Bubble Sort, Recursion, etc.
"""

# ===================== Module 1: Basic Imports & Abstract Base Class (OOP Core) =====================
# Function: Import essential modules, define abstract base user class (enforce abstract method implementation, encapsulate user attributes)
from datetime import datetime
from abc import ABC, abstractmethod

# Abstract Base Class: User Abstract Class (Courseware Abstract Class/ABC Concept)
class BaseUser(ABC):
    """Abstract base class for all users, enforces implementation of abstract methods and encapsulates core user attributes"""
    # Class Attribute: Count total number of user instances (Courseware Class Attribute Concept)
    total_users = 0

    def __init__(self, user_id, name, email):
        self.__user_id = user_id  # Private Attribute: Encapsulation (Courseware Encapsulation Concept)
        self.__name = name
        self.__email = email
        BaseUser.total_users += 1  # Increment class attribute to count instances

    # Encapsulation: Getter method to access private attribute
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    # Abstract Method: Enforce implementation in subclasses (Courseware Abstraction Concept)
    @abstractmethod
    def user_type(self):
        pass

    # Class Method: Operate on class attributes (Courseware Class Method Concept)
    @classmethod
    def show_total_users(cls):
        print(f"Total users on platform: {cls.total_users}")

    # Static Method: No dependency on class/instance attributes (Courseware Static Method Concept)
    @staticmethod
    def is_valid_id(uid):
        return isinstance(uid, int) and uid > 0

# ===================== Module 2: User/Book/Order/Node Classes (Data Models) =====================
# Function: Define Seller/Buyer subclasses (inherit from abstract base class), Book class, Order class, Linked List Node class (Data Structure)
class Seller(BaseUser):
    """Seller subclass inheriting from BaseUser, encapsulates list of books published by seller"""
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__published_books = []  # Private Attribute: Encapsulate books published by seller

    def user_type(self):  # Implement abstract method
        return "Seller"

    def add_published_book(self, book):
        self.__published_books.append(book)

    def get_published_books(self):
        return self.__published_books

class Buyer(BaseUser):
    """Buyer subclass inheriting from BaseUser, encapsulates list of orders placed by buyer"""
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__purchase_orders = []  # Private Attribute: Encapsulate buyer's orders

    def user_type(self):  # Implement abstract method
        return "Buyer"

    def add_order(self, order):
        self.__purchase_orders.append(order)

    def get_orders(self):
        return self.__purchase_orders

class Book:
    """Book class, encapsulates book attributes and implements magic methods (__str__/__eq__)"""
    # Class Attribute: Count total number of book instances
    total_books = 0

    def __init__(self, book_id, title, author, price, seller_id, status="available"):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__price = round(price, 2)  # Round price to 2 decimal places
        self.__seller_id = seller_id
        self.__status = status
        Book.total_books += 1

    # Magic Method: Format string output (Courseware __str__ Concept)
    def __str__(self):
        return f"[{self.__book_id}] {self.__title} by {self.__author} | Price: ¥{self.__price} | Status: {self.__status} | Seller ID: {self.__seller_id}"

    # Magic Method: Compare equality of two book objects (Courseware __eq__ Concept)
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__book_id == other.__book_id

    # Encapsulation: Getter/Setter methods
    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        if new_status in ["available", "reserved", "sold"]:
            self.__status = new_status

class Order:
    """Order class, encapsulates order attributes and implements magic method __str__"""
    # Class Attribute: Count total number of order instances
    total_orders = 0

    def __init__(self, order_id, book, buyer_id, status="pending"):
        self.__order_id = order_id
        self.__book = book
        self.__buyer_id = buyer_id
        self.__status = status
        self.__create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Order.total_orders += 1

    def __str__(self):  # Magic Method: Format string output
        return f"[{self.__order_id}] Book: {self.__book.get_title()} | Buyer ID: {self.__buyer_id} | Status: {self.__status} | Created at: {self.__create_time}"

    # Encapsulation: Getter/Setter methods
    def get_order_id(self):
        return self.__order_id

    def get_book(self):
        return self.__book

    def get_buyer_id(self):
        return self.__buyer_id

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        if new_status in ["pending", "completed", "cancelled"]:
            self.__status = new_status

class Node:
    """Linked List Node Class (Courseware Data Structure - Node Concept), stores Book objects"""
    def __init__(self, data):
        self.data = data  # Data field: Book object
        self.next = None  # Pointer field: Reference to next node

# ===================== Module 3: Transaction History Class (Encapsulate Transaction Logs) =====================
# Function: Manage all order records, provide methods to add/display transaction history
class TransactionHistory:
    """Transaction History class, encapsulates transaction logs and provides methods to add/display records"""
    def __init__(self):
        self.__transaction_records = []  # Private Attribute: Encapsulate transaction records

    def add_transaction(self, order):
        """Add a new order to transaction history"""
        self.__transaction_records.append(order)

    def display_history(self):
        """Display all transaction records"""
        if not self.__transaction_records:
            print("No transaction records found!")
            return
        print("\n===== Transaction History ======")
        for record in self.__transaction_records:
            print(record)
        print("==============================\n")

# ===================== Module 4: Algorithm Tool Class (Search/Sort/Recursion) =====================
# Function: Implement all required algorithms from courseware (Linear/Binary Search, Selection/Bubble Sort, Recursive Factorial)
class AlgorithmTool:
    """Algorithm Tool Class: Static methods for Linear Search, Binary Search, Selection Sort, Bubble Sort, Recursive Factorial"""
    # Static Method: Linear Search (Courseware Linear Search Concept, Time Complexity O(n))
    @staticmethod
    def linear_search(li, target, by="id"):
        """
        Linear Search for books
        :param li: Book list/Linked List head node
        :param target: Search target (ID/Title)
        :param by: Search criteria (id/title)
        :return: Found Book object or None
        """
        if isinstance(li, Node):  # Handle Linked List
            current = li
            while current:
                book = current.data
                if by == "id" and book.get_book_id() == target:
                    return book
                elif by == "title" and book.get_title() == target:
                    return book
                current = current.next
        else:  # Handle List
            for book in li:
                if by == "id" and book.get_book_id() == target:
                    return book
                elif by == "title" and book.get_title() == target:
                    return book
        return None

    # Static Method: Binary Search (Courseware Binary Search Concept, Time Complexity O(logn))
    @staticmethod
    def binary_search(sorted_book_list, target_id):
        """
        Binary Search for books (only works on ID-sorted list)
        :param sorted_book_list: Book list sorted by ID
        :param target_id: Target book ID
        :return: Found Book object or None
        """
        left = 0
        right = len(sorted_book_list) - 1
        while left <= right:
            mid = (left + right) // 2  # Middle index
            mid_book = sorted_book_list[mid]
            if mid_book.get_book_id() == target_id:
                return mid_book
            elif mid_book.get_book_id() < target_id:
                left = mid + 1
            else:
                right = mid - 1
        return None

    # Static Method: Selection Sort (Courseware Selection Sort Concept, Time Complexity O(n²))
    @staticmethod
    def selection_sort(book_list, ascending=True):
        """
        Selection Sort: Sort books by price
        :param book_list: List of Book objects
        :param ascending: True for ascending order, False for descending
        :return: Sorted book list
        """
        if len(book_list) <= 1:
            return book_list
        books = book_list.copy()
        n = len(books)
        for i in range(n - 1):
            min_max_idx = i
            # Find index of minimum/maximum value
            for j in range(i + 1, n):
                if ascending:
                    if books[j].get_price() < books[min_max_idx].get_price():
                        min_max_idx = j
                else:
                    if books[j].get_price() > books[min_max_idx].get_price():
                        min_max_idx = j
            # Swapping (Courseware Swapping Concept: a,b = b,a)
            books[i], books[min_max_idx] = books[min_max_idx], books[i]
        return books

    # Static Method: Bubble Sort (Courseware Bubble Sort Concept, Time Complexity O(n²))
    @staticmethod
    def bubble_sort(book_list, ascending=True):
        """
        Bubble Sort: Sort books by price
        :param book_list: List of Book objects
        :param ascending: True for ascending order, False for descending
        :return: Sorted book list
        """
        if len(book_list) <= 1:
            return book_list
        books = book_list.copy()
        n = len(books)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):
                if ascending:
                    if books[j].get_price() > books[j + 1].get_price():
                        books[j], books[j + 1] = books[j + 1], books[j]
                        swapped = True
                else:
                    if books[j].get_price() < books[j + 1].get_price():
                        books[j], books[j + 1] = books[j + 1], books[j]
                        swapped = True
            if not swapped:  # Early termination: List is already sorted
                break
        return books

    # Static Method: Recursive Factorial (Courseware Recursion Concept)
    @staticmethod
    def factorial(n):
        """Recursive Factorial Implementation (Base Case + Recursive Step)"""
        if n == 0 or n == 1:  # Base Case
            return 1
        return n * AlgorithmTool.factorial(n - 1)  # Recursive Step

# ===================== Module 5: Marketplace Core Class (Integrate All Functions) =====================
# Function: Integrate core business logic (book management, order processing, algorithm calls, statistics display)
class Marketplace:
    """Core Marketplace Class for Campus Second-hand Book Trading, integrates OOP and algorithm concepts"""
    def __init__(self):
        self.__book_head = None  # Book Inventory: Linked List Head Node (Courseware Linked List Concept)
        self.__order_list = []   # Order List
        self.__book_id_counter = 1
        self.__order_id_counter = 1
        self.__transaction_log = TransactionHistory()
        self.__algo_tool = AlgorithmTool()  # Algorithm Tool Instance

    def _linklist_to_list(self):
        """Private Method: Convert linked list to list for sorting/searching"""
        book_list = []
        current = self.__book_head
        while current:
            book_list.append(current.data)
            current = current.next
        return book_list

    def add_book(self, title, author, price, seller_id):
        """Add new book to marketplace (Linked List Append), with input validation"""
        if not title or not author:
            print("\n❌ Title and Author cannot be empty!")
            return None
        if price <= 0:
            print("\n❌ Price must be greater than 0!")
            return None
        # Create Book object
        new_book = Book(self.__book_id_counter, title, author, price, seller_id)
        # Linked List Append (Tail Insertion)
        new_node = Node(new_book)
        if not self.__book_head:  # Empty Linked List
            self.__book_head = new_node
        else:  # Non-empty Linked List, find tail node
            current = self.__book_head
            while current.next:
                current = current.next
            current.next = new_node
        # Increment ID counter (with recursive factorial demo)
        self.__book_id_counter += 1
        print(f"\n✅ Book '{title}' added successfully! Book ID: {new_book.get_book_id()}")
        return new_book

    def view_all_books(self):
        """View all books in marketplace (Traverse Linked List)"""
        book_list = self._linklist_to_list()
        if not book_list:
            print("\n📚 No books available in marketplace!")
            return
        print("\n===== All Available Books =====")
        for book in book_list:
            print(book)
        print("===============================\n")

    def place_order(self, book_id, buyer_id):
        """Place order for a book: Linear Search for book, update status"""
        # Linear Search for book (Courseware Concept)
        target_book = self.__algo_tool.linear_search(self.__book_head, book_id, by="id")
        if not target_book or target_book.get_status() != "available":
            print("\n❌ Order failed! Book not found or already sold/reserved")
            return None
        # Create Order object
        new_order = Order(self.__order_id_counter, target_book, buyer_id)
        self.__order_list.append(new_order)
        self.__order_id_counter += 1
        # Update book status to reserved
        target_book.set_status("reserved")
        # Record transaction
        self.__transaction_log.add_transaction(new_order)
        print(f"\n✅ Order created successfully! Order ID: {new_order.get_order_id()}")
        return new_order

    def cancel_order(self, order_id):
        """Cancel pending order: Linear Search for order, update order/book status"""
        # Linear Search for order
        target_order = None
        for order in self.__order_list:
            if order.get_order_id() == order_id and order.get_status() == "pending":
                target_order = order
                break
        if not target_order:
            print("\n❌ Cancellation failed! Order not found or already completed/cancelled")
            return False
        # Update order and book status
        target_order.set_status("cancelled")
        target_order.get_book().set_status("available")
        # Update transaction history
        self.__transaction_log.add_transaction(target_order)
        print(f"\n✅ Order {order_id} has been cancelled!")
        return True

    def sort_books_by_price(self, sort_algorithm="selection", ascending=True):
        """Sort books by price: Support Selection Sort/Bubble Sort"""
        book_list = self._linklist_to_list()
        if not book_list:
            print("\n📚 No books available to sort!")
            return []
        # Call sorting methods from AlgorithmTool
        if sort_algorithm == "selection":
            sorted_books = self.__algo_tool.selection_sort(book_list, ascending)
        elif sort_algorithm == "bubble":
            sorted_books = self.__algo_tool.bubble_sort(book_list, ascending)
        else:
            print("\n❌ Invalid algorithm! Defaulting to Selection Sort")
            sorted_books = self.__algo_tool.selection_sort(book_list, ascending)
        # Print sorted results
        print(f"\n===== Books Sorted by Price ({'Ascending' if ascending else 'Descending'} - {sort_algorithm} sort) =====")
        for book in sorted_books:
            print(book)
        print(f"===========================================================================\n")
        return sorted_books

    def search_book(self, target, by="id", search_algorithm="linear"):
        """Search for books: Support Linear Search/Binary Search"""
        book_list = self._linklist_to_list()
        if not book_list:
            print("\n📚 No books available in marketplace!")
            return None
        # Binary Search only supports ID-based search with sorted list
        if search_algorithm == "binary":
            if by != "id":
                print("\n❌ Binary Search only supports ID-based search! Defaulting to Linear Search")
                return self.__algo_tool.linear_search(self.__book_head, target, by)
            # Sort books by ID before Binary Search
            sorted_by_id = sorted(book_list, key=lambda x: x.get_book_id())
            target_book = self.__algo_tool.binary_search(sorted_by_id, target)
        else:
            # Linear Search
            target_book = self.__algo_tool.linear_search(self.__book_head, target, by)
        # Print search results
        if target_book:
            print(f"\n✅ Book found: {target_book}")
        else:
            print(f"\n❌ Target book not found!")
        return target_book

    def view_order_history(self):
        """View all transaction records"""
        self.__transaction_log.display_history()

    def show_statistics(self):
        """Display platform statistics: Call class attributes"""
        print("\n===== Platform Statistics =====")
        print(f"Total Users: {BaseUser.total_users}")
        print(f"Total Books: {Book.total_books}")
        print(f"Total Orders: {Order.total_orders}")
        print("==============================\n")

# ===================== Module 6: Main Program Entry (Interactive Interface) =====================
# Function: Provide console interactive menu, integrate all user operation entrances
def main():
    """Main Program Entry: Console Interactive Menu (Modular Programming Concept)"""
    # Initialize marketplace
    campus_market = Marketplace()
    # Pre-create test users
    test_seller = Seller(1, "Zhang San", "seller@campus.edu")
    test_buyer = Buyer(2, "Li Si", "buyer@campus.edu")
    # Print welcome message
    print("🎉 Campus Second-hand Book Trading Platform (COMP 2090SEF) 🎉")
    print(f"📌 Test Seller ID: {test_seller.get_user_id()} | Test Buyer ID: {test_buyer.get_user_id()}")
    print(f"📌 Seller Type: {test_seller.user_type()} | Buyer Type: {test_buyer.user_type()}\n")

    # Main menu loop
    while True:
        print("===== Campus Second-hand Book Trading Platform Menu =====")
        print("1. Add new book for sale")
        print("2. View all available books")
        print("3. Place order for a book")
        print("4. Cancel an existing order")
        print("5. View transaction history")
        print("6. Sort books by price (Selection/Bubble Sort)")
        print("7. Search for a book (Linear/Binary Search)")
        print("8. View platform statistics")
        print("0. Exit program")
        print("==========================================================")

        # Input validation (Exception Handling)
        try:
            choice = int(input("Please enter operation number: "))
        except ValueError:
            print("\n❌ Invalid input! Please enter a numeric value\n")
            continue

        # Function branches
        if choice == 1:
            # Add new book
            print("\n----- Add New Book -----")
            try:
                seller_id = int(input("Enter seller ID: "))
                if not BaseUser.is_valid_id(seller_id):
                    print("\n❌ Seller ID must be a positive integer!")
                    continue
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                price = float(input("Enter book price (¥): "))
                campus_market.add_book(title, author, price, seller_id)
            except ValueError:
                print("\n❌ Invalid input! Price must be a numeric value\n")

        elif choice == 2:
            # View all books
            campus_market.view_all_books()

        elif choice == 3:
            # Place order
            print("\n----- Place Order -----")
            try:
                book_id = int(input("Enter book ID to purchase: "))
                buyer_id = int(input("Enter buyer ID: "))
                if not (BaseUser.is_valid_id(book_id) and BaseUser.is_valid_id(buyer_id)):
                    print("\n❌ IDs must be positive integers!")
                    continue
                campus_market.place_order(book_id, buyer_id)
            except ValueError:
                print("\n❌ Invalid input! IDs must be numeric values\n")

        elif choice == 4:
            # Cancel order
            print("\n----- Cancel Order -----")
            try:
                order_id = int(input("Enter order ID to cancel: "))
                if not BaseUser.is_valid_id(order_id):
                    print("\n❌ Order ID must be a positive integer!")
                    continue
                campus_market.cancel_order(order_id)
            except ValueError:
                print("\n❌ Order ID must be a numeric value\n")

        elif choice == 5:
            # View transaction history
            campus_market.view_order_history()

        elif choice == 6:
            # Sort books by price (Selection/Bubble)
            print("\n----- Sort Books by Price -----")
            algo_choice = input("Select sorting algorithm (1-Selection Sort / 2-Bubble Sort): ")
            sort_choice = input("Select sort order (1-Ascending / 2-Descending): ")
            algo = "selection" if algo_choice == "1" else "bubble"
            ascending = True if sort_choice == "1" else False
            campus_market.sort_books_by_price(sort_algorithm=algo, ascending=ascending)

        elif choice == 7:
            # Search for books (Linear/Binary)
            print("\n----- Search for Book -----")
            by_choice = input("Select search criteria (1-Book ID / 2-Book Title): ")
            algo_choice = input("Select search algorithm (1-Linear Search / 2-Binary Search): ")
            by = "id" if by_choice == "1" else "title"
            algo = "linear" if algo_choice == "1" else "binary"
            try:
                target = int(input(f"Enter book {by} to search: ")) if by == "id" else input(f"Enter book {by} to search: ").strip()
                campus_market.search_book(target, by=by, search_algorithm=algo)
            except ValueError:
                print("\n❌ Book ID must be a numeric value!")

        elif choice == 8:
            # View platform statistics
            campus_market.show_statistics()
            BaseUser.show_total_users()

        elif choice == 0:
            # Exit program
            print("\n👋 Thank you for using COMP 2090SEF Book Trading Platform! Goodbye!")
            break

        else:
            print("\n❌ Invalid operation number! Please try again\n")

# ===================== Program Startup Entry =====================
# Function: Ensure execution only when run as main program (Core of Modular Programming)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n⚠️  Program error occurred: {str(e)}")
        print("Please check your input or restart the program!")