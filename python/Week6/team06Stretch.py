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

class Circle:

    def __init__(self):
        self.center = Point
        selfradius = 0.

    def prompt_for_circle(self):
        self.center.prompt_for_point(self)
        self.radius = input("Enter radius: ")

    def display(self):
        print("Center:")
        self.center.display(self)
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