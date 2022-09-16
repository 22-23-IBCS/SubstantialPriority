import random

class Favanimal:
    
    def __init__(self, name, col, size, weight):
        self.name = name
        self.spec = "dog"
        self.col = col
        self.size = size
        self.weight = weight
        
    def getName(self):
        return self.name 
        
    def getSize(self):
        return self.size
    
    def getColor(self):
        return self.col
    
    def changeColor(self, col2):
        self.col = col2
        
    def randomSize(self):
        size = ["xs","s","m","l","xl"]
        self.size = size[random.randint(0,4)]
        
        
    
def main():
    gold_re = Favanimal("Golden Retriever", "dark gold", "m", "65")
    pom = Favanimal("Pomernian", "white", "s", "13")
    
    print(gold_re.getName(), gold_re.getSize(), gold_re.getColor())
    print(pom.getName(), pom.getSize(), pom.getColor()) 
    print("\nname, size, and color different")
    
    print("\nvalues changing"+"-"*50+"\n")
    
    gold_re.changeColor("brown")
    print(gold_re.getName(), gold_re.getSize(), gold_re.getColor())

    pom.randomSize()
    print(pom.getName(), pom.getSize(), gold_re.getColor())     

if __name__ == "__main__":
    main()