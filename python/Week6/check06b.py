class Phone:
    """Parent class that has 3 member variables and 2 methods"""

    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def display(self):
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))

class SmartPhone(Phone):
    """Child class of Phone that includes the member variables from Phone as well as an email address"""

    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        Phone.prompt_number(self)
        self.email = input("Email: ")

    def display(self):
        Phone.display(self)
        print(self.email)

def main():
    newPhone = Phone()
    newCell = SmartPhone()
    print("Phone:")
    newPhone.prompt_number()
    print()
    newPhone.display()
    print()
    print("Smart phone:")
    newCell.prompt()
    print()
    newCell.display()

if __name__ == "__main__":
    main()