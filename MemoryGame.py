import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = None

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        user_list = []
        print("Remember these numbers:")
        print(self.sequence)
        time.sleep(0.7)
        print("\n" * 100)  # Clearing the console
        print("Now enter the numbers you remember:")
        for _ in range(self.difficulty):
            while True:
                try:
                    user_input = int(input("Enter a number: "))
                    user_list.append(user_input)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        return user_list

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        self.generate_sequence()
        user_input = self.get_list_from_user()
        if self.is_list_equal(self.sequence, user_input):
            print("Congratulations! You remembered all the numbers correctly!")
            return True
        else:
            print("Oops! You missed some numbers. Better luck next time!")
            return False

# Example usage:
if __name__ == "__main__":
    difficulty = 5  # Set the difficulty level here
    game = MemoryGame(difficulty)
    game.play()