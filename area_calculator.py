from math import pi, sqrt


class Shape:
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self) -> str:
        return f"The Area of {self.__class__.__name__} is {self.get_area()}: "

class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

class Square(Shape):
    def __init__(self,side1, side2 = None):
        super().__init__(side1, side1 or side2)

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(side1 = base, side2 = height)

    def get_area(self):
        area = super().get_area()
        return area / 2 #its return the area of the triangle

class Circle(Shape):
    def __init__(self,radius):
        super().__init__(side1 = radius, side2 = radius)

    def get_area(self):
        return pi * (self.side1 * self.side2)

class Pentagon(Shape):
    def __init__(self,height,side):
        super().__init__(side1 = height, side2 = side)

    def get_area(self):
        return (self.side1 * self.side2) / 2    

class Hexagon(Shape):
    def __init__(self,side1, side2 = None):
        super().__init__(side1, side1 or side2)

    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2 


welcome_message = "----welcome to area calculator"
print(welcome_message.upper())
print("-" * len(welcome_message))
main = True
while main:
    print("whic shape wold you like to calculate?")
    print("""
    1 - Rectangle
    2 - Circle
    3 - Triangle
    4 - Square
    5 - Pentagon
    6 - Hexagon
    Please enter 0 to Exit...
    """)
    while True:
        try:
            choice = int(input("Please enter your choice: "))
            
            if choice == 1:
                print("You choose Rectangle")
                side_1 = float(input("Enter the first side of the Rectangle: "))
                side_2 = float(input("Enter the second side of the Rectangle: "))
                rectangle = Rectangle(side_1, side_2)
                print(rectangle.__str__())

            elif choice == 2:
                print("You choose Cicle")
                radius = float(input("Please enter the radius of the Circle: "))
                circle = Circle(radius)
                print(circle.__str__())

            elif choice == 3:
                print("You choose Triangle")
                base = float(input("Please enter the base of Triangle: "))
                height = float(input("Please enter the height of the Triange: "))
                triangle = Triangle(base, height)
                print(triangle.__str__())

            elif choice == 4:
                print("You choose Square")
                side = float(input("Please enter the side of Square: "))
                square = Square(side)
                print(square.__str__())

            elif choice == 5:
                print("You choose Pentagon")
                height = float(input("Please enter of the height of the Pentagon: "))
                side = float(input("Please enter the side of the Pentagon: "))
                pentagon = Pentagon(height, side)
                print(pentagon.__str__())

            elif choice == 6:
                print("You choose Hexagon")
                side = float(input("Please enter og the side of the Hexagon: "))
                hexagon = Hexagon(side)
                print(hexagon.__str__())

            elif choice == 0:
                break

            break
        except ValueError:
            print("Please enter an integer number")                        
