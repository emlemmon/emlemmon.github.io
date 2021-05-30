from collections import deque


class Student:
    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

    def display(self):
        print("{}, {}")

class HelpSystem:
    def __init__(self):
        self.waiting_list = deque()

    def is_student_waiting(self):
        if len(self.waiting_list) > 0:
            return True
        else:
            return False
    
    def add_to_waiting_list(self, student):
        self.waiting_list.append(student)

    def help_next_student(self):
        if self.is_student_waiting():
            current_student = self.waiting_list.popleft()
            print("Now helping {} with {}".format(current_student.name, current_student.course))
        else:
            print("No one to help.")
            print()

def main():
    newHelpSystem = HelpSystem()
    prompt = ""
    while prompt != "3":
        print("Options:")
        print("1. Add a new student")
        print("2. Help next student")
        print("3. Quit")
        prompt = input("Enter selection: ")
        print()

        if prompt == "1":
            newStudent = Student()
            newStudent.prompt()
            newHelpSystem.add_to_waiting_list(newStudent)

        elif prompt == "2":
            newHelpSystem.help_next_student()
        
        elif prompt == "3":
            print("Goodbye.")

if __name__ == "__main__":
    main()