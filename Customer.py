import pandas as pd

df = pd.read_csv('customer.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

def getFirstName(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'first name']

    except:
        return False

def setFirstName(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 0] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getLasttName(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'last name']

    except:
        return False

def setLastName(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 1] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getShippingAddress(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'shipping address']

    except:
        return False

def setShippingAddress(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 2] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getCity(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'city']

    except:
        return False

def setCity(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 3] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getState(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'state']

    except:
        return False

def setState(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 4] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getZipCode(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'zip code']

    except:
        return False

def setZipCode(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 5] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False


def getUsername(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'username']

    except:
        return False

def setUsername(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 6] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getPassword(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'password']

    except:
        return False

def setPassword(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 7] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getPhoneNumber(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'phone number']

    except:
        return False

def setPhoneNumber(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 8] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getEmail(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'email']

    except:
        return False

def setEmail(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 9] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getCreditCard(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'credit card']

    except:
        return False

def setCreditCard(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 10] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getCVC(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'cvc']

    except:
        return False

def setCVC(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 11] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def getExpirationDate(key):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        return df.at[row, 'expiration date']

    except:
        return False

def setExpirationDate(key, value):
    try:
        global df
        row = df[df['customer id'] == key].index[0]
        df.iat[row, 12] = value
        df.to_csv('customer.csv', header = True, index = False)

    except:
        return False

def login(key, value):
    try:
        global df
        row = df[df['username'] == key].index[0]
        if (df.at[row, 'password'] == value):
            return True
        return False

    except:
        return False

def forgotPassword(key):
    try:
        global df
        row = df[df['username'] == key].index[0]
        return df.at[row, 'password']

    except:
        return False



