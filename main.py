from random import choice
from string import ascii_lowercase


class Hangman:
    def __init__(self, words, attempts):
        self.guessed_letters = set()
        self.total_letters = set()
        self.wort = choice(words)
        self.attempts = attempts

    # replaces the hyphens with the guessed characters
    def replace_hyphen(self):
        return "".join([char if char in self.guessed_letters else "-" for char in self.wort])

    # checks input for mistakes and evaluates whether character is in word or not
    def evaluate_input(self, letter):
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif letter in self.total_letters:
            print("You already typed this letter")
        elif letter in self.wort:
            self.guessed_letters.add(letter)
            self.total_letters.add(letter)
        else:
            print("No such letter in the word")
            self.total_letters.add(letter)
            self.attempts -= 1

    def is_finished(self):
        return "-" not in self.replace_hyphen()

    # actual game loop
    def game(self):
        print("H A N G M A N")
        while self.attempts > 0:
            print("\n" + self.replace_hyphen())
            letter_spieler = input("Input a letter: > ")
            self.evaluate_input(letter_spieler)
            if self.is_finished():
                print("\n" + self.wort)
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You are hanged!")

    # starts game dependent on user entry
    def menu(self):
        mode = input('Type "play" to play the game, "exit" to quit: > ')
        if mode == "play":
            self.game()
        else:
            return 0

# creation of an object every time the game starts
if __name__ == "__main__":
    while True:
        game_1 = Hangman(("python", "java", "kotlin", "javascript"), 8)
        if game_1.menu() == 0:
            break
