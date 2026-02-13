class Item:
    def __init__(self, name, description, price, owner):
        self.name = name
        self.description = description
        self.price = price
        self.owner = owner
        self.is_sold = False

    def __str__(self):
        return f"{self.name}: {self.description}, Price: {self.price}, Owner: {self.owner}, Sold: {self.is_sold}"

    def sell(self):
        self.is_sold = True


class User:
    def __init__(self, username, contact):
        self.username = username
        self.contact = contact
        self.items_for_sale = []

    def add_item(self, item):
        self.items_for_sale.append(item)

    def remove_item(self, item):
        self.items_for_sale.remove(item)

    def __str__(self):
        return f"User: {self.username}, Contact: {self.contact}"


class Marketplace:
    def __init__(self):
        self.items = []
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def search_item(self, name):
        results = [item for item in self.items if name.lower() in item.name.lower()]
        return results

    def list_all_items(self):
        return self.items


# 使用範例
if __name__ == "__main__":
    marketplace = Marketplace()

    # 創建用戶
    user1 = User("Alice", "alice@example.com")
    marketplace.add_user(user1)

    # 創建物品
    item1 = Item("二手書", "Python 程式設計", 300, user1.username)
    user1.add_item(item1)
    marketplace.add_item(item1)

    # 列出所有物品
    for item in marketplace.list_all_items():
        print(item)

    # 搜尋物品
    search_results = marketplace.search_item("Python")
    for result in search_results:
        print("搜尋到的物品:", result)
