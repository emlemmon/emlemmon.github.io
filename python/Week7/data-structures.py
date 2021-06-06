def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fib(n - 1) + fib(n - 2))

def main():
    newNum = int(input("Enter a Fibonnoci index: "))
    print("The Fibonnoci number is: {}".format(fib(newNum)))

if __name__ == "__main__":
    main()