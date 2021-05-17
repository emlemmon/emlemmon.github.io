

class Robot:
    """Class for creating robots that can move"""

    MOVEMENT = 1
    FIRE_COST = 15
    MOVE_COST = 5
    
    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100
    
    def use_fuel(self, amount):
        """Checks and decrements fuel_amount, returns True if there was enough fuel"""
        if self.fuel_amount >= amount:
            self.fuel_amount -= amount
            return True
        else:
            print("Insufficient fuel to perform action")
            return False

    def move_left(self):   
        """Moves left if there is enough fuel"""
        if self.use_fuel(Robot.MOVE_COST):
            self.x_coordinate -= Robot.MOVEMENT

    def move_right(self):   
        """Moves right if there is enough fuel"""     
        if self.use_fuel(Robot.MOVE_COST):
            self.x_coordinate += Robot.MOVEMENT

    def move_up(self): 
        """Moves up if there is enough fuel"""       
        if self.use_fuel(Robot.MOVE_COST):
            self.y_coordinate -= Robot.MOVEMENT

    def move_down(self):
        """Moves down if there is enough fuel"""        
        if self.use_fuel(Robot.MOVE_COST):
            self.y_coordinate += Robot.MOVEMENT   

    def check_status(self):
        """Prints the x and y coordinates and the fuel_amount"""
        print("({}, {}) - Fuel: {}".format(self.x_coordinate, self.y_coordinate, self.fuel_amount))
    
    def fire(self):
        """Prints "Pew! Pew! if there is enough fuel"""
        if self.use_fuel(Robot.FIRE_COST):
            print("Pew! Pew!")

def main():
    """Accepts comments from the user until "quit" is entered"""
    newRobot = Robot()
    prompt = ""
    while prompt.lower() != "quit":
        prompt = input("Enter command: ")
        if prompt.lower() == "left":
            newRobot.move_left()
        elif prompt.lower() == "right":
            newRobot.move_right()
        elif prompt.lower() == "up":
            newRobot.move_up()
        elif prompt.lower() == "down":
            newRobot.move_down()
        elif prompt.lower() == "fire":
            newRobot.fire()
        elif prompt.lower() == "status":
            newRobot.check_status()
    print("Goodbye.")

if __name__ == "__main__":
    main()