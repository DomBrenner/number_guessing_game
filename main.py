import random

while True:
    random_num = random.randint(1, 100)
    user_input = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\nEnter your choice: ")

    if user_input == "1":
        difficulty = "easy"
        guesses = 10
    elif user_input == "2":
        difficulty = "medium"
        guesses = 5
    elif user_input == "3":
        difficulty = "hard"
        guesses = 3
    else:
        print("Invalid choice. Please restart and select 1, 2, or 3.")
        break

    print(f"Great! You have selected the {difficulty} difficulty level.")
    print("Let's start the game!")

    attempt = 1

    while guesses > 0:
        user_guess = int(input("Enter your guess: "))
        if user_guess == random_num:
            print(f"Congratulations! You guessed the correct number in {attempt} attempts")
            break
        elif user_guess < random_num:
            print(f"Incorrect! The number is greater than {user_guess}.")
        else:
            print(f"Incorrect! The number is less than {user_guess}.")
        attempt += 1
        guesses -= 1
    else:
        print(f"You failed to guess the number. The number was {random_num}")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break