class Book:
    def __init__(self, title, author, ISBN, genre, price, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def title(self):
        return self.title

    def author(self):
        return self.author

    def ISBN(self):
        return self.ISBN

    def genre(self):
        return self.genre

    def price(self):
        return self.price

    def quantity(self):
        return self.quantity

    def setQuantity(self, num):
        self.quantity = num
        return
