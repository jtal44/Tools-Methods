import pandas as pd

df = pd.read_csv('book.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

def searchCatagory(category, key):
    global df
    category = category.lower()
    try:
        print(df[(df[category] == key)])

    except:
        print("No books found")

def decrease(isbn, num):
    global df
    row = df[df['isbn'] == isbn].index[0]
    q = df.at[row, 'quantity']
    if q < num:
        return False
    df.iat[row, 4] = q - num
    df.to_csv('book.csv', header=True, index=False)

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
