import random


def play_round():
    secret = random.randint(1, 10)  # system picks a number from 1 to 10

    while True:
        guess = input("Guess a number between 1 and 10: ").strip()
        if guess.isdigit() and 1 <= int(guess) <= 10:
            guess = int(guess)
            break
        print("Please enter a whole number from 1 to 10.")

    if guess == secret:
        print(f"You win! The number was {secret}.")
        return True
    print(f"Sorry, you lose. The number was {secret}.")
    return False


def main():
    print("=== Guess the Number ===")
    wins = rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1
        print(f"Score: {wins} win(s) out of {rounds} round(s)\n")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
