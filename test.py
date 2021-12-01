#Shopping cart isn't going to be an object so you don't need to use __init__. The shopping cart should be some sort of
#list or a file you store books in. Down below I have code to create a list that has books stored in it. When you add a
#book to the shopping cart you should take in an ISBN and compare it to the ISBN of the books in this list using the
#.ISBN function from Book.py. For displaying just print out the title, price, and quantity for the books being purchased
#along with their index or row number next to them. For the remove function call your display function and prompt the
#user for the index/row number of the item they would like to remove and how many of that item they would like to remove
#from their cart. For checkout display shopping cart and the total price then get the user to approve the purchase.

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
book_list = [book1, book2, book3, book4, book5]