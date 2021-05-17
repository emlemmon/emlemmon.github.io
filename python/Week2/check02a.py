
def prompt_number():
    user_num = int(input("Enter a positive number: "))
    while user_num < 0:
        print("Invalid entry. The number must be positive.")
        user_num = int(input("Enter a positive number: "))
    print()
    return user_num


def compute_sum(first, second, third):
    return first + second + third

def main():
    first_num = prompt_number()
    second_num = prompt_number()
    third_num = prompt_number()
    sum = compute_sum(first_num, second_num, third_num)
    print("The sum is: " + str(sum))

if __name__ == "__main__":
    main()
