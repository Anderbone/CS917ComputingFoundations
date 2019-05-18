import random
import re

"""This game plays hangman with the user."""


class Hangman:

    def __init__(self):
        self.hidden_word = self.find_word()
        self.blank_string = "-" * len(self.hidden_word)
        self.lives = 6

        # For debugging only ;)
        print(self.hidden_word)

        print(self.blank_string)

    def process_guess2(self, guess):
        list1 = []
        for i in re.finditer(guess, self.hidden_word):
            list1.append(i.start())

        return list1


    def find_word(self):
        # This method is complete
        dictionary = open('C:/Users/yanch/Documents/dataForCode/words', 'r')
        words = list(dictionary)
        return random.choice(words).lower().strip()

    def draw_hangman(self, lives):
        if lives == 6:
            print("=========\n ||     |\n ||\n ||\n ||\n ||\n/  \\")

        elif lives == 5:
            print("=========\n ||     |\n ||     O\n ||\n ||\n ||\n/  \\")

        elif lives == 4:
            print("=========\n ||     |\n ||     O\n ||     |\n ||\n ||\n/  \\")

        elif lives == 3:
            print("=========\n ||     |\n ||    \O\n ||     |\n ||\n ||\n/  \\")

        elif lives == 2:
            print("=========\n ||     |\n ||    \O/\n ||     |\n ||\n ||\n/  \\")

        elif lives == 1:
            print("=========\n ||     |\n ||    \O/\n ||     |\n ||    /\n ||\n/  \\")

        elif lives == 0:
            print("=========\n ||     |\n ||     O \n ||    /|\\\n ||    / \\\n ||\n/  \\")


    def won_game(self):
          # Your code here (this should be called from play)
        print('you won!')
        exit()


    def play(self):
         # Your code here
        ans_now = list(self.blank_string)
        while True:
            this_guess = input('guess one please\n')
            change = self.process_guess2(this_guess)
            if change != []:
                for i in change:
                    ans_now[i] = (this_guess)
                if(ans_now == list(self.hidden_word)):
                    self.won_game()
                print(ans_now)
                print('now you have %d lives' % self.lives)
                print('good one, continue')
            else:
                print('wrong one')
                print(ans_now)
                self.lives -= 1
                print('now you have %d lives' % self.lives)

            self.draw_hangman(self.lives)
            if (self.lives == 0):
                print('you lose!!')
                break

if __name__ == "__main__":
    game = Hangman()
    game.play()