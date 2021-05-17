class Student:
    """student class for creating new students ids"""
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.idNum = 0

def prompt_student():
    student1 = Student()
    student1.firstName = input("Please enter your first name: ")
    student1.lastName = input("Please enter your last name: ")
    student1.idNum = input("Please enter your id number: ")
    return student1

def display_student(student):
    print()
    print("Your information:")
    print(str(student.idNum + " - " + student.firstName + " " + student.lastName))

def main():
    user = prompt_student()
    display_student(user)

if __name__ == "__main__":
    main()
