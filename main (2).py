from models import Seller, Buyer, Book
from marketplace import Marketplace

def draw_menu():
    print("\n╔════════════════════════════════════╗")
    print("║   Second-Hand Book Marketplace v1.0 ║")
    print("╚════════════════════════════════════╝")
    print("1. Add Book (as Seller)")
    print("2. View Available Listings")
    print("3. Place Order (using sample buyer)")
    print("4. Cancel Oldest Waitlist Order")
    print("5. View Transaction History")
    print("6. Get Price-based Recommendations")
    print("0. Exit")
    print()

def main():
    marketplace = Marketplace()

    seller1 = Seller("Alice", "alice@email.com", "S001")
    buyer1  = Buyer("Bob",   "bob@email.com",   "B001")

    marketplace.add_book(Book("Python Programming", 20, "Good"))
    marketplace.add_book(Book("Clean Code", 35, "Like New"))
    marketplace.add_book(Book("Introduction to Algorithms", 85, "Acceptable"))

    while True:
        draw_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                title = input("Enter book title: ").strip()
                price = float(input("Enter price (HKD): "))
                condition = input("Enter condition (e.g. Good, Like New): ").strip()
                book = Book(title, price, condition)
                print(marketplace.add_book(book))
            except ValueError:
                print("Invalid price. Please enter a number.")

        elif choice == "2":
            print("\nAvailable Books:")
            print(marketplace.view_listings() or "None")

        elif choice == "3":
            if not any(b.available for b in marketplace.books):
                print("No available books to order.")
                continue

            print("\nAvailable books:")
            for book in marketplace.books:
                if book.available == True:
                    print(str(number)+". "+ book.title + " — $"+ str(round(book.price, 2))+ " ("+ book.condition + ")")
            number = number + 1

            try:
                idx = int(input("\nEnter number of book to buy: ")) - 1
                available = [b for b in marketplace.books if b.available]
                if 0 <= idx < len(available):
                    book = available[idx]
                    print(marketplace.place_order(buyer1, book))
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print(marketplace.cancel_order())

        elif choice == "5":
            hist = marketplace.history.display()
            if not hist:
                print("No completed transactions yet.")
            else:
                print("\nTransaction History:")
                for line in hist:
                    print(line)

        elif choice == "6":
            print("\n" + marketplace.recommend_with_radix())

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
