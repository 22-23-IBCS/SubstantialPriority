class Coffeeshop2:

    def __init__(self):
        self.items = {"Cafe Americano":2.5, "Cafe Latte":3.0, "Cappuccino":3.5,
                      "Frappucino":4.5, "Caramel Macchiato":4.25,
                      "Iced Coffee":3.0, "Hot Coffee":3.25, "Bagel":1.5, "Egg Benedict":6.5}
        
        self.inventory = {"Cafe Americano":10, "Cafe Latte":10, "Cappuccino":10,
                      "Frappucino":10, "Caramel Macchiato":10,
                      "Iced Coffee":10, "Hot Coffee":10, "Bagel":10, "Egg Benedict":10}

        self.totalPrice = 0
        self.info = "The cofee shop is founded by one student from Annie Wright school \nand is rated the #1 coffee shop in the world by Forbes 2022\nwith the cheapeast price."
        self.orders = []


        self.menu = list(self.items.keys())
        self.price = list(self.items.values())

        self.storename = "Expresso Express"
        self.storemanager = "Justin"

        
    def calcPrice(self):
        for i in self.orders:
            self.totalPrice = self.totalPrice + self.items[i]
            
        return self.totalPrice

    def calcLeft(self, order):

        numleft = self.inventory.get(order) - 1
        
        if numleft >= 0:
            self.inventory.update({order:numleft})
            return False

        else:
            print("\nSorry. We do not have that much.")
            return True

    def addOrder(self,new_order):                
        if new_order in self.items:
            self.orders.append(str(new_order))
        else:
            print("We do not have that.")

    def subOrder(self, wrong_order):
        self.orders.remove(wrong_order)

    def showMenu(self):
        return self.menu

    def showPrice(self):
        return self.price
    
    def getinfo(self):
        return self.info

    
            

def main():

    EE = Coffeeshop2()
    menu = Coffeeshop2().showMenu()

    menu = EE.showMenu()
    price = EE.showPrice()

    
    orders = input("Welcome to Expresso Express! What do you want to order?\n1 to see the menu, 2 to see the information about the shop \n")
    if orders == "1":
        print("Here is the menu")
        count = 0
        for i in range(len(menu)):
                count += 1
                print(str(count) + " " + menu[i] + " : " + str(price[i]) + "$")
                
    elif orders == "2":
        print(EE.getinfo())
        print("\nLet's order now you must be hungry.")
        count = 0
        for i in range(len(menu)):
            count += 1
            print(str(count) + " " + menu[i] + " : " + str(price[i]) + "$")
        

    more = "Y"
    while more != "N":
        more = input("\nDo you want to order something (one each time)? Y or N\n")
        if more == "Y":
            order = input("\nWhat do you want me to add? ")
            if order in list(EE.showMenu()):
                num = int(input("How many of them? "))
                count = 0
                for i in range(num):
                    notleft = EE.calcLeft(order)
                    if notleft:
                        print("You can still order this %d times." %(count))
                        still = input("Do you want to do so? Y or N\n")
                        if still == "Y":
                            break
                        elif still == "N":
                            for i in range(count):
                                EE.subOrder(order)
                        else:
                            print("Undefined Command. Please try again. Choose betwween Y or N.")
                        break
                    count += 1
                    EE.addOrder(order)
                        
            else:
                print("Sorry. We do not have that menu. Please try again.")
        elif more == "N":
            print("We will have your order.")
        else:
            print("Undefined command. Please try again.")


    total = EE.calcPrice()
    print("\nThe total price is {} dollars. Thanks for coming. \nDon't forget to rate us 5 stars.".format(total))
    





if __name__ == "__main__":
    main()
