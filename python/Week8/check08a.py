class GPA:
    def __init__(self):
        self.gpa = 0.0

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, value):
        if value < 0:
            self.gpa = 0
        elif value > 4:
            self.gpa = 4
        else:
            self.gpa = value

    def get_letter(self):
        if self.gpa == 0 or self.gpa < 1:
            return "F"
        elif self.gpa == 1 or self.gpa < 2:
            return "D"
        elif self.gpa == 2 or self.gpa < 3:
            return "C"
        elif self.gpa == 3 or self.gpa < 4:
            return "B"
        else:
            return "A"

    def set_letter(self, value):
        if value == "A":
            self.gpa = 4.0
        elif value == "B":
            self.gpa = 3.0
        elif value == "C":
            self.gpa = 2.0
        elif value == "D":
            self.gpa = 1.0
        elif value == "F":
            self.gpa = 0.0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()