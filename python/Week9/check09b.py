class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message) 

def get_inverse(n):
    try:
        n = int(n)
        if n == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero")
        elif n < 0:
            raise NegativeNumberError("Error: The value cannot be negative")
        else:
            return 1/n
    except ValueError as ex:
        raise ValueError("Error: The value must be a number")


def main():
    num = 0
    try:
        num = input("Enter a number: ")
        print("The result is: " + str(get_inverse(num)))
    except ZeroDivisionError as ex:
            print("{}".format(str(ex)))
    except NegativeNumberError as ex:
            print("{}".format(str(ex)))
    except ValueError as ex:
            print("{}".format(str(ex)))

if __name__ == "__main__":
    main()