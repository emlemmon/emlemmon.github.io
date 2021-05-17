class Date:

    def __init__(self):
        self.day = 1
        self.month = 1
        self.month = 2000

    def prompt(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))

    #def pad(self, date):
    #    if int(date) > 10:
    #       date = "0" + str(date)
    #    return date

    def display(self):
        print("{}/{}/{}".format(self.month, self.day, self.year))


