#Class : ShoppingCart
#addToShoppingCart, viewShoppingCart,  checkOut, remove, totalPrice

class ShoppingCart:

    def __inti__(self, itemName, itemPrice, itemQuantity):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity

    def addtoCart(self, itemName, itemQuantity, itemPrice):
        for i in cartItems:
            itemName = i[0]
            itemQuantity = i[1]
            itemPrice = i[2]

            if itemName in cartItems:
                cartItems[itemName][0] += itemQuantity
                cartItems[itemName][1] = itemPrice

            else:
                cartItem[itemName] = [itemQuantity, itemPrice]

    def removefromCart(self, itemName, itemQuantity):
        for i in cartItems:
            itemName = i[0]
            itemQuantity = i[1]

            if itemName in cartItems:
                if cartItems[itemName][0] > itemQuantity:
                    cartItems[itemName][0] -= itemQuantity
                if cartItems[itemName][0] <= 0:
                    del cartItems[itemName]

    def totalPrice(self, itemName, itemQuantity):
        sum = 0
        for i in cartItems:
            itemName = i[0]
            itemQuantity = i[1]

            if itemName in cartItems:
                if cartItems[itemName][0] > itemQuantity:
                    sum += cartItems[itemName][1]*itemQuantity
                    cartItems[itemName][0] -= itemQuantity
                if cartItems[itemName][0] <= 0:
                    del cartItems[itemName]
        return sum

    def viewShoppingCart():
        for i in cartItems:
            print(i, 'quantity=' , cartItems[i][0], 'price= ', cartItems[i][1])
        
    def checkOut():
        pass
