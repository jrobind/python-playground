# Hangman game using the CLI. A word is selected from a pre-made list, and the user should
# attempt to guess the word with a limited number of attempts. Only one letter is to be
# submitted by the user at a time. 

import os

class Hangman(object):
    def __init__(self, difficulty):
        # source words depending on difficulty
        self.difficulty = difficulty
        self.word = self.source_word(difficulty)
        self.guesses_made = 0
        self.correct_guess = False
        self.letter_guesses = []
        self.word_guesses = []
        # run game
        self.run_game()

    def source_word(self, difficulty):
        folder = os.path.dirname(os.path.abspath(__file__))

        if (difficulty == 'easy'):
            f = open(os.path.join(folder, "words_easy.txt"), "r")
        else:
            f = open("words_hard.txt", "r")

    def run_game(self):
        while (not(self.correct_guess)):
            self.get_guesses()

    def get_guesses(self):
        self.guesses_made += 1
        self.letter_guesses.append(raw_input('Please guess the first letter of the word: '))
        # run checks
        self.run_checks()
    
    def run_checks(self):
        if (self.guesses_made > 0):
            self.word_guesses.append(raw_input(
                'Current guessed letters: ' + self.format_letters(self.letter_guesses) + ' Please guess the word:  '))
            # loop over guesses to check if any are correct
            for guess in self.word_guesses:
                if (guess == self.word):
                    self.correct_guess = True
                    self.winMessage()
            
    def format_letters(self, letters):
        return  ' '.join(letters)

    def winMessage(self):
        print('Well done! You guessed correct! The correct word is ' + self.word)

# initiate game
diff = raw_input('Welcome to Hangman, please select a diffculty: Easy or Hard ')
Hangman(diff)