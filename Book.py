class Book:
    def __init__(self, title, author, ISBN, genre, price, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.price = price
        self.quantity = quantity

    @property
    def title(self):
        return self.title

    @property
    def author(self):
        return self.author

    @property
    def ISBN(self):
        return self.ISBN

    @property
    def genre(self):
        return self.genre

    @property
    def price(self):
        return self.price

    @property
    def quantity(self):
        return self.quantity




