from Inventory import *
from Customer import *
from ShoppingCart import *

def search(customer_id):
    while True:
        print()
        print("1. View all books")
        print("2. Search by category")
        print("3. Add book to cart")
        print("4. Back to previous menu")
        print("5. Exit program")
        cin = input(">> ")

        if cin == "1":
            viewAll()

        elif cin == "2":
            print("Title\nAuthor\nISBN\nGenre")
            category = input("Please enter the category you would like to search:")
            key = input("Search: ")
            searchCatagory(category, key)

        elif cin == "3":
            isbn = input("Enter ISBN of the book you would like to purchase: ")
            quantity = input("Enter the amount you would like to purchase: ")

            addtoCart(isbn, quantity)

        elif cin == "4":
            return

        elif cin == "5":
            exit()

        else:
            print("Invalid input please enter the number next to the option you would like to choose!")

def account(customer_id):
    while True:
        print()
        print("1. Change Password")
        print("2. Change Address")
        print("3. Change Card info")
        print("4. Change Email")
        print("5. Change Phone Number")
        print("6. Delete Account")
        print("7. Back to previous menu")
        print("8. Exit program")
        cin = input(">> ")

        if cin == "1":
            cur = getPassword(customer_id)
            print("Current Password:", cur)
            new = input("New Password: ")
            check = setPassword(customer_id, new)
            if check == False:
                print("close customer.csv and try again")

        elif cin == "2":
            cur_addr = getShippingAddress(customer_id)
            cur_city = getCity(customer_id)
            cur_state = getState(customer_id)
            cur_zip = getZipCode(customer_id)
            print("Current Address:", cur_addr, cur_city, ",", cur_state, cur_zip)

            new_addr = input("New Street Address: ")
            setShippingAddress(customer_id, new_addr)
            new_city = input("New City: ")
            setCity(customer_id, new_city)
            new_state = input("New State (abbreviated): ")
            setState(customer_id, new_state)
            new_zip = input("New Zip Code: ")
            check = setZipCode(customer_id, new_zip)
            if check == False:
                print("close customer.csv and try again")

        elif cin == "3":
            cur_card = getCreditCard(customer_id)
            cur_ccv = getCVC(customer_id)
            cur_exp = getExpirationDate(customer_id)
            print("Current Credit Card:", cur_card, cur_ccv, cur_exp)

            new_card = input("New Card Number: ")
            setCreditCard(customer_id, new_card)
            new_ccv = input("New ccv: ")
            setCVC(customer_id, new_ccv)
            new_exp = input("New Expiration Date: ")
            check = setExpirationDate(customer_id, new_exp)
            if check == False:
                print("close customer.csv and try again")

        elif cin == "4":
            cur = getEmail(customer_id)
            print("Current Email:", cur)
            new = input("New Email: ")
            check = setEmail(customer_id, new)
            if check == False:
                print("close customer.csv and try again")

        elif cin == "5":
            cur = getPhoneNumber(customer_id)
            print("Current Phone Number:", cur)
            new = input("New Phone Number: ")
            check = setPhoneNumber(customer_id, new)
            if check == False:
                print("close customer.csv and try again")

        elif cin == "6":
            confirm = input("\nAre you sure that you would like to delete your account? (y/n): ")
            confirm = confirm.lower()
            if confirm == "y":
                check = deleteAccount(customer_id)
                if check == False:
                    print("close customer.csv and try again")
                return True

        elif cin == "7":
            return False

        elif cin == "8":
            exit()

        else:
            print("Invalid input please enter the number next to the option you would like to choose!")

def shoppingCart(customer_id):
    print("\n1. View cart")
    print("2. Remove item")
    print("3. Checkout")
    print("4. Back to previous menu")
    print("5. exit()")
    cin = input(">> ")

    if cin == "1":
        viewCart()

    elif cin == "2":
        removefromCart()

    elif cin == "3":
        checkout()

        i = 0
        while i < len(cart):
            isbn = cart[i].ISBN
            quantity = cart[i].quantity
            check = decrease(isbn, quantity)
            if check == False:
                print("One of the items you are trying to purchase is out of stock. Please remove:", isbn)
                return
            else:
                setPurchaseHistory(customer_id, isbn, quantity)
            i += 1

    elif cin == "4":
        return

    elif cin == "5":
        exit()

    else:
        print("Invalid input please enter the number next to the option you would like to choose!")

def menu2(customer_id):
    if customer_id == False:
        print("Invalid username or password.")
        return

    while True:
        first = getFirstName(customer_id)
        last = getLasttName(customer_id)
        print()
        print("welcome", first, last)
        print("1. Search for book")
        print("2. Purchase History")
        print("3. Edit Account")
        print("4. Shopping Cart")
        print("5. Logout")
        print("6. Exit program")
        cin = input(">> ")

        if cin == "1":
            search(customer_id)

        elif cin == "2":
            getPurchaseHistory(customer_id)

        elif cin == "3":
            deleted = account(customer_id)
            if deleted == True:
                return

        elif cin == "4":
            shoppingCart(customer_id)

        elif cin == "5":
            return

        elif cin == "6":
            exit()

        else:
            print("Invalid input please enter the number next to the option you would like to choose!")

df = pd.read_csv('book.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

while True:
    print()
    print("Welcome to the Book Store!")
    print("1. Login")
    print("2. Create Account")
    print("3. Forgot Password")
    print("4. Exit program")
    menu1 = input(">> ")

    if menu1 == "1":
        username = input("Username: ")
        password = input("Password: ")
        customer_id = login(username, password)
        menu2(customer_id)

    elif menu1 == "2":
        customer_id = createAccount()
        setFirstName(customer_id, input("\nPlease enter your first name: "))
        setLastName(customer_id, input("\nPlease enter your last name: "))
        setUsername(customer_id, input("\nPlease enter the username you would like to use: "))
        setPassword(customer_id, input("\nPlease enter the password you would like to use: "))
        setCreditCard(customer_id, input("\nPlease enter a credit card number: "))
        setCVC(customer_id, input("\nPlease enter the ccv for the credit card: "))
        setExpirationDate(customer_id, input("\nPlease enter the card's expiration date: "))
        setShippingAddress(customer_id, input("\nPlease enter the street address that you would like your packages shipped to: "))
        setCity(customer_id, input("\nPlease enter your City: "))
        setState(customer_id, input("\nPlease enter your State: "))
        setZipCode(customer_id, input("\nPlease enter your zip code: "))
        setEmail(customer_id, input("\nPlease enter your email address: "))
        setPhoneNumber(customer_id, input("\nPlease enter your phone number: "))
        print("\nYour account has now been created!")
        menu2(customer_id)

    elif menu1 == "3":
        username = input("Username: ")
        print(forgotPassword(username))

    elif menu1 == "4":
        exit()

    else:
        print("Invalid input please enter the number next to the option you would like to choose!")
