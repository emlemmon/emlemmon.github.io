class RationalNum:
    """ Class for creating rational numbers"""
    def __init__(self):
        self.numerator = 0
        self.denominator = 0

    def display(self):
        integar = 0
        while int(self.numerator) >= int(self.denominator):
            self.numerator = int(self.numerator) - int(self.denominator)
            integar += 1
        if integar > 0:
            print(str(integar) + " " + str(self.numerator) + "/" + str(self.denominator))
        else:
            print(str(self.numerator) + "/" + str(self.denominator))
        
    def reduce(self):
        if int(self.denominator) % int(self.numerator) 

    def prompt(self):
        self.numerator = input("Enter the Numerator: ")
        self.denominator = input("Enter the Denominator: ")

    def display_decimal(self):
        print(int(self.numerator) / int(self.denominator))

def main():
    newFraction = RationalNum()
    newFraction.numerator = 1
    newFraction.denominator = 2
    newFraction.display()
    newFraction.prompt()
    newFraction.display()
    newFraction.display_decimal()

if __name__ == "__main__":
    main()