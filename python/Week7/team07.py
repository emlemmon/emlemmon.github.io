from abc import ABC
from abc import abstractmethod

class Employee(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod 
    def display(self):
        print(self.name)

class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourlyWage = 0

    def display(self):
        print("{} - ${}/hour".format(self.name, self.hourlyWage))

class SalaryEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 0

    def display(self):
        print("{} - ${}/year".format(self.name, self.salary))

def main():

    employees = []
    userInput = input("Please enter h, s, or q: ")
    while userInput != "q":
  
        if userInput == "h":
            newHourly = HourlyEmployee()
            newHourly.name = input("Enter name: ")
            newHourly.hourlyWage = input("Enter hourly wage: ")
            employees.append(newHourly)
            userInput = input("Please enter h, s, or q: ")

        elif userInput == "s":
            newSalary = SalaryEmployee()
            newSalary.name = input("Enter name: ")
            newSalary.salary = input("Enter salary wage: ")
            employees.append(newSalary)
            userInput = input("Please enter h, s, or q: ")

    for x in employees:
        x.display()

if __name__ == "__main__":
    main()