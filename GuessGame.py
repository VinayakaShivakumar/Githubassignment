import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print("Please enter a number within the specified range.")
            except ValueError:
                print("Please enter a valid number.")

    def compare_results(self, guess):
        if guess == self.secret_number:
            print("Congratulations! You guessed the correct number!")
            return True
        else:
            print("Oops! That's not the correct number.")
            return False

    def play(self):
        self.generate_number()
        while True:
            user_guess = self.get_guess_from_user()
            if self.compare_results(user_guess):
                return True
            else:
                continue

# Main function to run the game
def main():
    while True:
        difficulty = int(input("Enter the difficulty level (an integer greater than 1): "))
        game = GuessGame(difficulty)
        game.play()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
