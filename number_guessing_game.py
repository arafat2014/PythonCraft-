import random

def play_game():
    number_to_guess = random.randint(1, 50)
    attempts = 0

    print("Guess a number between 1 and 50")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

play_game()
