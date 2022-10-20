class Vehicle:
    
    #constructor method, Needed to defind how the class instances are created
    def __init__(self, brand, col): 
        self.numWheels = 4
        self.brand = brand
        self.color = col
        
    def getBrand(self):
        return self.brand

    def setBrand(self, b):
        self.brand = b
        
class Truck(Vehicle):

    def __init__(self, b, col):
        super().__init__(b, col)



def main():





if __name__ == "__main__":
    main()
