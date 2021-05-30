class Point:
    """Class that has 2 member variables and 2 methods"""

    def __init__(self):
        self.x = 0.
        self.y = 0.

    def prompt_for_point(self):
        self.x = input("Enter x: ")
        self.y = input("Enter y: ")

    def display(self):
        print("({}, {})".format(self.x, self.y))

class Circle(Point):
    """Class that inherits from the parent class of Point and adds another member variable"""

    def __init__(self):
        super().__init__()
        self.radius = 0.

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = input("Enter radius: ")

    def display(self):
        print("Center:")
        Point.display(self)
        print("Radius: {}".format(self.radius))

def main():
    newPoint = Point()
    newCircle = Circle()

    newPoint.prompt_for_point()
    newPoint.display()
    newCircle.prompt_for_circle()
    newCircle.display()

if __name__ == "__main__":
    main()