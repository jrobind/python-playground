# Hangman game using the CLI. A word is selected from a pre-made list, and the user should
# attempt to guess the word with a limited number of attempts. Only one letter is to be
# submitted by the user at a time. 

class Hangman(object):
    def __init__(self):
        # render inital game command
        self.guesses_made = 0
        self.correct_guess = False
        self.letter_guesses = []
        self.word_guesses = []
        # run game
        self.run_game()

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

    def format_letters(self, letters):
        return  ' '.join(letters)

# initiate game
Hangman()