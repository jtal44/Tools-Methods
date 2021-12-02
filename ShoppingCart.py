import Book as bk
import pandas as pd

df = pd.read_csv('book.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

book1 = bk.Book(df.iat[0, 0], df.iat[0, 2], df.iat[0, 1], df.iat[0, 3], df.iat[0, 5], df.iat[0, 4])
book2 = bk.Book(df.iat[1, 0], df.iat[1, 2], df.iat[1, 1], df.iat[1, 3], df.iat[1, 5], df.iat[1, 4])
book3 = bk.Book(df.iat[2, 0], df.iat[2, 2], df.iat[2, 1], df.iat[2, 3], df.iat[2, 5], df.iat[2, 4])
book4 = bk.Book(df.iat[3, 0], df.iat[3, 2], df.iat[3, 1], df.iat[3, 3], df.iat[3, 5], df.iat[3, 4])
book5 = bk.Book(df.iat[4, 0], df.iat[4, 2], df.iat[4, 1], df.iat[4, 3], df.iat[4, 5], df.iat[4, 4])
stock = [book1, book2, book3, book4, book5]

cart = []


def addtoCart(isbn, quantity):
    global cart

    i = 0
    while i < 5:
        if isbn == stock[i].ISBN:
            cart.append(stock[i])

            cartlength = len(cart) - 1
            cart[cartlength].setQuanitity(quantity)

            return
        i += 1
    print("Could not find ISBN number.  Please try again.")


def viewCart():
    global cart
    i = 0
    while i < len(cart):
        print(cart[i].title, cart[i].author, cart[i].price, cart[i].quantity)
        i = +1
    return


def removefromCart():
    global cart

    viewCart()
    isbnRem = input("Please enter the ISBN number of the item you want to remove: ")

    i = 0
    while i < 5:
        if isbnRem == stock[i].ISBN:
            cart.remove(stock[i])
            print("Item has been removed from the cart.")
            return
        i = +1
    print("Could not find ISBN number.  Please try again.")


def totalPrice():
    global cart

    i = 0
    priceT = 0
    while i < len(cart):
        priceT = priceT + cart[i].price
        i = +1

    print("Total Price is " + priceT)


def checkout():
    global cart

    viewCart()
    totalPrice()

    while True:
        inputConfirm = input("Are you ready to confirm your purchase? Y for yes, N for No: ")

        if inputConfirm == "Y":
            return True
        elif inputConfirm == "N":
            return False
        else:
            print("Invalid Input. Please try again.")