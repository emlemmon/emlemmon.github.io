class GPA:
    def __init__(self):
        self._gpa = 0.0

    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, value):
        if value < 0:
            self._gpa = 0
        elif value > 4:
            self._gpa = 4
        else:
            self._gpa = value

    gpa = property(_get_gpa, _set_gpa)

    @property
    def letter(self):
        return self._get_letter()
    
    @letter.setter
    def letter(self, value):
        return self._set_letter(value)
    
    def _get_letter(self):
        if self._gpa < 1:
            return "F"
        elif self._gpa < 2:
            return "D"
        elif self._gpa < 3:
            return "C"
        elif self._gpa < 4:
            return "B"
        else:
            return "A"


    def _set_letter(self, value):
        if value == "A":
            self._gpa = 4.0
        elif value == "B":
            self._gpa = 3.0
        elif value == "C":
            self._gpa = 2.0
        elif value == "D":
            self._gpa = 1.0
        elif value == "F":
            self._gpa = 0.0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()