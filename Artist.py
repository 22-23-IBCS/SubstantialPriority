import turtle
import math
    
class Artist():

    def __init__(self, t):
        self.t = t

    def Triangle(self, size):
        for i in range(3):
            self.t.fd(size)
            self.t.rt(120)

    def Square(self, size):
        for i in range(4):
            self.t.fd(size)
            self.t.rt(90)

    def Circle(self, radius=100):
        self.t.circle(radius)

    def Star(self, size=100):
        for i in range(5):
            self.t.fd(size)
            self.t.rt(144)
            self.t.fd(size)
            self.t.lt(72)
        
    def Polygon(self, sides, size):
        if sides<3:
            print("Shape has to have at least 3 sides")
        else:
            angle = 180*(sides-2) / sides
            for i in range(sides):
                self.t.fd(size)
                self.t.rt(180-angle)

    def unknown1(self):
        colors = ["red", "blue", "green", "purple"]
        for i in range(200):
            self.t.circle(i)
            self.t.lt(90)
            self.t.color(colors[i%4])

    def unknown2(self,size):
        colors = ["red", "green"]
        col_count = 0
        while (True):
          col_count += 1
          self.t.color(colors[col_count%2])
          self.t.fd(size)
          self.t.rt(91)
          size += 1
    

            


def main():

    bg = turtle.Screen()
    bg.title("Artist")
    t = turtle.Turtle()
    art = Artist(t)
    t.speed(5)
    
    art.Triangle(60)
    t.clear()

    art.Square(60)
    t.clear()

    art.Circle()
    t.clear()

    art.Star()
    t.clear()
    
    art.Polygon(10,50)
    t.clear()

    t.speed(0)
    
    art.unknown1()
    t.clear()
    
    art.unknown2(5)
    
    







if __name__ == "__main__":
    main()
