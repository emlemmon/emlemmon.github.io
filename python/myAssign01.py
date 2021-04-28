import random
from random import randint
print("Welcome to the number guessing game!")
seed_value = input("Enter random seed: ")
random.seed(seed_value)
print()

def guessing_game():
    num = randint(1,100)
    count = 1
    user_guess = -1
    while user_guess != num:
        user_guess = int(input("Please enter a guess: "))
        if user_guess > num:
            print("Lower")
            print()
            count += 1
        elif user_guess < num:
            print("Higher")
            print()
            count += 1

    print("Congratulations. You guessed it!")
    print("It took you " + str(count) + " guesses.")
    print()
    play_again = input("Would you like to play again (yes/no)? ")
    if play_again == "yes":
        print()
        guessing_game()
    else:
        print("Thank you. Goodbye.")

guessing_game()