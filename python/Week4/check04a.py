class Person:
    """creates a Person object"""
    def __init__(self):
        self.name = "anonymous"
        self.birthYear = "unknown"

    def display(self):
        print("{} (b. {})".format(self.name, self.birthYear))

class Book:
    """creates a Book object"""
    def __init__(self):
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"

    def display(self):
        print(self.title)
        print("Publisher:")
        print(self.publisher)
        print("Author:")
        self.author.display()

def main(): 
    """Creates an instance of the book class, takes user input and displays the new book information"""
    newBook = Book()
    newBook.display()
    print()
    
    print("Please enter the following:")
    newBook.author.name = input("Name: ")
    newBook.author.birthYear = input("Year: ")
    newBook.title = input("Title: ")
    newBook.publisher = input("Publisher: ")
    print()
    newBook.display()

if __name__ == "__main__":
    main()