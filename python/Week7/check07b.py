"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self):
        self.name = ""
    
    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))
    
    @abstractmethod 
    def get_area(self):
        return float

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0.0

    def get_area(self):
        return 3.14 * self.radius * self.radius 

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"
        self.length = 0.0
        self.width = 0.0

    def get_area(self):
        return self.length * self.width

def main():

    shapes = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            newCircle = Circle()
            newCircle.radius = radius
            shapes.append(newCircle)
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            newRect = Rectangle()
            newRect.length = length
            newRect.width = width
            shapes.append(newRect)

    # Done entering shapes, now lets print them all out:
    for x in shapes:
        x.display()
    #TODO: Loop through each shape in the list, and call its display function


if __name__ == "__main__":
    main()

