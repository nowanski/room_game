import random

# create a function that will generate a random number
def generate_random_number():
    return random.randint(1, 100)

# create a function that will get user input
def get_user_input():
    return int(input("Enter a number (1-100): "))

# create a function that will compare the user input to the random number,if the user input is greater than the random number, return "too high", if the user input is less than the random number, return "too low", if the user input is equal to the random number, return "you win"
def compare_user_input_to_random_number(user_input, random_number):
    if user_input > random_number:
        print("too high")
        return False
    elif user_input < random_number:
        print("too low")
        return False
    else:
        print("you win")
        return True

# create a function that will run the game, first print friendly message, then generate a random number, then get user input, then compare user input to random number, then if the user input is not equal to the random number, repeat the process until the user input is equal to the random number
def run_game():
    print("Welcome to the number guessing game!")
    random_number = generate_random_number()
    user_input = get_user_input()
    while not compare_user_input_to_random_number(user_input, random_number):
        user_input = get_user_input()
    print("Thank you for playing!")

if __name__ == "__main__":
    run_game()