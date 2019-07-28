# Hangman game using the CLI. A word is selected from a pre-made list, and the user should
# attempt to guess the word with a limited number of attempts. Only one letter is to be
# submitted by the user at a time. 

import os
import random


class Hangman(object):
    """A Hangman game class.
    User inputs difficulty (easy or hard) which initates game.
    """
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
        dir_path = './game_data'

        if (difficulty == 'easy'):
            file = open(r'%s/words_easy.txt' % dir_path)
            # format words into readable string
            words = file.read().replace('\n', ' ').split()
            return self.random_word_gen(words)
        else:
            file = open(r'%s/words_hard.txt' % dir_path)
            words = file.read().replace('\n', ' ').split()
            return self.random_word_gen(words)

    def run_game(self):
        while (not(self.correct_guess)):
            self.get_guesses()

    def random_word_gen(self, words):
        index = random.randint(0, len(words))
        return words[index]

    def get_guesses(self):
        self.guesses_made += 1
        self.letter_guesses.append(raw_input('Please guess the first letter of the word: '))
        # run checks
        self.run_checks()
    
    def run_checks(self):
        if (self.guesses_made > 0):
            self.word_guesses.append(raw_input(
                'Current guessed letters: {} Please guess the word: '.format(self.format_letters(self.letter_guesses))))
            # loop over guesses to check if any are correct
            for guess in self.word_guesses:
                if (guess == self.word):
                    self.correct_guess = True
                    self.winMessage()

            if (self.fail_message().lower() == 'no'):
                self.correct_answer_message()
            
    def fail_message(self):
        return raw_input("Sorry, that's incorrect. Would you like to try again? ")

    def correct_answer_message(self):
        print('The correct word is {}'.format(self.word))
        self.correct_guess = True
    
    def format_letters(self, letters):
        return  ' '.join(letters)

    def win_message(self):
        print('Well done! You guessed correct! The correct word is {} '.format(self.word))
        self.correct_guess = True

# initiate game
diff = raw_input('Welcome to Hangman, please select a diffculty: Easy or Hard ')
Hangman(diff.lower())