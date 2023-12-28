import unittest


class Bookstore:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, quantity, price):
        self.inventory[title] = {"quantity": quantity, "price": price}

    def check_stock(self, title):
        return self.inventory.get(title, {"quantity": 0})["quantity"]

    def calculate_total_price(self, title, quantity):
        book_info = self.inventory.get(title)
        if book_info:
            return book_info["price"] * quantity
        return 0

    def sell_book(self, title, quantity):
        if title in self.inventory and self.inventory[title]["quantity"] >= quantity:
            self.inventory[title]["quantity"] -= quantity
            return f"{quantity} {title}(s) sold."
        return "Insufficient stock."

    def restock_book(self, title, quantity):
        if title in self.inventory:
            self.inventory[title]["quantity"] += quantity
            return f"{quantity} {title}(s) restocked."
        return "Book not found."

    def remove_book(self, title):
        if title in self.inventory:
            del self.inventory[title]
            return f"{title} removed from inventory."
        return "Book not found in inventory."


class TestBookStore(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore()
        self.bookstore.add_book("Python Crash Course", 10, 25)
        self.bookstore.add_book("Data Science Handbook", 5, 35)

    def test_check_stock(self):
        self.assertEqual(self.bookstore.check_stock("Python Crash Course"), 10)

    def test_calculate_total_price(self):
        self.assertEqual(
            self.bookstore.calculate_total_price("Python Crash Course", 3), 75
        )

    def test_sell_book(self):
        self.assertEqual(
            self.bookstore.sell_book("Python Crash Course", 3),
            "3 Python Crash Course(s) sold.",
        )

    def test_restock_book(self):
        self.assertEqual(
            self.bookstore.restock_book("Python Crash Course", 5),
            "5 Python Crash Course(s) restocked.",
        )
        self.assertEqual(self.bookstore.check_stock("Python Crash Course"), 15)

    def test_remove_book(self):
        self.assertEqual(
            self.bookstore.remove_book("Data Science Handbook"),
            "Data Science Handbook removed from inventory.",
        )
        self.assertEqual(self.bookstore.check_stock("Data Science Handbook"), 0)


if __name__ == "__main__":
    unittest.main()
