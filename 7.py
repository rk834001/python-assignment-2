class Book:
    def init(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.price -= (self.price * discount_percentage / 100)

class EBook(Book):
    def init(self, title, author, price, format):
        super().init(title, author, price)
        self.format = format

    def display(self):
        book_info = super().display()
        return f"{book_info}, Format: {self.format}"

# Example usage:
book1 = Book("Python Programming", "John Smith", 25.0)
book2 = EBook("Web Development", "Jane Doe", 20.0, "PDF")

print(book1.display())
book1.apply_discount(10)
print(book1.display())

print(book2.display())
book2.apply_discount(15)
print(book2.display())
