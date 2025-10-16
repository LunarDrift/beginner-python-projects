import random

play_again = "yes"

while play_again.lower() == "yes":

    n = random.randint(1, 100)
    max_guesses = 0
    guess = None
    guesses = 1

    print("Welcome to the Number Guessing Game!\n")
    print("Choose your difficulty\n")
    print("1. Easy (10 guesses) \n2. Medium (5 guesses) \n3. Hard (3 guesses)\n")

    difficulty_valid = False
    while not difficulty_valid:
        try:
            difficulty = int(input("Difficulty: "))       
            if difficulty == 1:
                max_guesses = 10
                difficulty_valid = True

            elif difficulty == 2:
                max_guesses = 5
                difficulty_valid = True

            elif difficulty == 3:
                max_guesses = 3
                difficulty_valid = True

            else:
                print("Invalid input. Choose a difficulty. 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You have {max_guesses} guesses to find the number.")

    while guess != n and guesses <= max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            
        except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        if guess < n:
                print("Too low! Try again!")
                guesses += 1

        elif guess > n:
                print("Too high! Try again!")
                guesses += 1

        else:
                print(f"Correct! You guessed the number in {guesses} tries!")

    if guess != n:
            print(f"\nGame over! You ran out of guesses. The number was {n}")

    play_again = input("\nDo you want to play again? (yes/no): ")

print("Thanks for playing!")

