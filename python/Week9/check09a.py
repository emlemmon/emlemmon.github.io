while True:
    try:
        n = input("Enter a number: ")
        n = int(n)
        break
    except ValueError:
        print("The value entered is not valid")
print("The result is: {}".format(n*2))