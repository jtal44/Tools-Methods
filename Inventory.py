import pandas as pd

df = pd.read_csv('book.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

def searchCatagory(category, key):
    global df
    print(df[(df[category] == key)])

def decrease(isbn):
    global df
    row = df[df['isbn'] == isbn].index[0]
    q = df.at[row, 'quantity']
    df.iat[row, 4] = q - 1
    df.to_csv('book.csv', header=True, index=False)
    print(df)

def checkStock():
    global df
    instock = df[df['quantity'] > 0]
    print(instock)

def viewAll():
    global df
    print(df)

def search(key):
    result = df[df == key]
    print(result)
