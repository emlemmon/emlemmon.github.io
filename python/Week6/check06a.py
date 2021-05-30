class Book:
    """parent class for different types of Books"""

    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = input("Publication Year: ")

    def display_book_info(self):
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))

class TextBook(Book):
    """Child class that extends Book class and adds a member variable and two methods"""

    def __init__(self):
        super().__init__()
        self.subject = ""
        
    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print("Subject: {}".format(self.subject))

class PictureBook(Book):
    """Child class that extends Book class and adds a member variable and two methods"""

    def __init__(self):
        self.illustrator = ""
        super().__init__()

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print("Illustrated by {}".format(self.illustrator))

def main():
    """runs the main code to create new Book objects"""

    newBook = Book()
    newBook.prompt_book_info()
    print()
    newBook.display_book_info()
    print()
    newText = TextBook()
    newText.prompt_book_info()
    newText.prompt_subject()
    print()
    newText.display_book_info()
    newText.display_subject()
    print()
    newPicture = PictureBook()
    newPicture.prompt_book_info()
    newPicture.prompt_illustrator()
    print()
    newPicture.display_book_info()
    newPicture.display_illustrator()

if __name__ == "__main__":
    main()