"""
This module represents some classes for a simple word game.

There are a number of incomplete methods in the which you must implement to make fully functional.

About the game board!
The board's tiles are indexed from 1 to N, and the first square (1,1) is in the top left.
A tile may be replaced by another tile, hence only one tile may occupy a space at any one time.

Author: Jiyu Yan.
Student ID:1851015
"""


class LetterTile:
    """ This class is complete. You do not have to do anything to complete this class """

    def __init__(self, letter):
        self.letter = letter.lower()

    def get_letter(self):
        """ Returns the letter associatedd with this tile. """
        return self.letter

    def get_score(self):
        """ Returns the score asscoiated with the letter tile """
        return {
            'a': 1,
            'b': 2,
            'c': 2,
            'd': 3,
            'e': 1,
            'f': 3,
            'g': 2,
            'h': 3,
            'i': 1,
            'j': 3,
            'k': 2,
            'l': 3,
            'm': 5,
            'n': 3,
            'o': 1,
            'p': 2,
            'q': 2,
            'r': 3,
            's': 1,
            't': 1,
            'u': 1,
            'v': 3,
            'w': 3,
            'x': 5,
            'y': 3,
            'z': 5
        }[self.letter]


class GameBoard:
    """ This class represents the gameboard itself.
        You are required to complete this class.
    """

    def __init__(self, width, height):
        """ The constructor for setting up the gameboard """
        self.width = width
        self.height = height
        self.board = [['-'] * self.width for i in range(self.height)]

    def set_tile(self, x, y, tile):
        """ Places a tile at a location on the board. """
        letter = tile.get_letter()
        self.board[x-1][y-1] = letter

    def get_tile(self, x, y):
        """ Returns the tile at a location on the board """
        return self.board[x-1][y-1]

    def remove_tile(self, x, y):
        """ Removes the tile from the board and returns the tile"""
        letter = self.board[x-1][y-1]
        self.board[x - 1][y - 1] = '-'
        return letter

    def get_words(self):
        """ Returns a list of the words on the board sorted in alphabetic order.
            The list of 'words' contains all words on the board.

            At first, we go right at each row, if a tile has a letter and the right next tile of it also has a letter,
            it has a word.Then we keep going right to see how long this word is, and append that word. After that
            we don't need to see these tiles we just go through.

            Second part is go down at each col, the idea is exactly same. we use 'xx'and 'yy' at this part.

        """
        words = []
        # go right at each row
        x = 0
        while x < self.height:
            y = 0
            while y < self.width:
                if self.board[x][y] != '-' and y + 1 < self.width and self.board[x][y + 1] != '-':
                    i = 1
                    word = [self.board[x][y]]
                    while y + i < self.width and self.board[x][y + i] != '-':
                        word.append(self.board[x][y + i])
                        i += 1
                    y = y + i
                    words.append(''.join(word))
                y += 1
            x += 1
        # now we go down at each col
        yy = 0
        while yy < self.width:
            xx = 0
            while xx < self.height:
                if self.board[xx][yy] != '-' and xx + 1 < self.height and self.board[xx + 1][yy] != '-':
                    ii = 1
                    word1 = [self.board[xx][yy]]
                    while xx + ii < self.height and self.board[xx + ii][yy] != '-':
                        word1.append(self.board[xx + ii][yy])
                        ii += 1
                    xx = xx + ii
                    words.append(''.join(word1))
                xx += 1
            yy += 1
        words.sort()
        return words

    def top_scoring_words(self):
        """ Returns a list of the top scoring words.
            If there is a single word, then the function should return a single item list.
            If multiple words share the highest score, then the list should contain the words sorted alphabetically.

            we have a def get_word_score which returns the score of a word.
            Then we sort all words in the board using this get_word_score def as a key. The top score word would be the
            first in sorted list.

            Finally we return multiple words share the highest score if the board has multiple highest score words.
        """
        wordslist = self.get_words()
        top_score_words = []

        def get_word_score(word):
            # return the score of a word, for example, 'demo' has score d:3 e:1 m:5 o:1 so it returns 10.
            word_score = 0
            for letter in word:
                word_score += LetterTile(letter).get_score()
            return word_score

        wordslist.sort(key=get_word_score, reverse=True)
        i = 0
        while get_word_score(wordslist[i]) == get_word_score(wordslist[0]):
            top_score_words.append(wordslist[i])
            i += 1
        top_score_words.sort()
        return top_score_words

    def print_board(self):
        """ Prints a visual representation of the board
            Please use the - character for unused spaces
        """
        for i in self.board:
            print('|'.join(i))

    def letters_placed(self):
        """ Returns a count of all letters currently on the board """
        count = 0
        for i in self.board:
            for letter in i:
                if letter != '-':
                    count += 1
        return count


if __name__ == "__main__":
    """ This is just a sample for testing you might want to add your own tests here """
    board = GameBoard(10, 10);

    d = LetterTile("d")
    e = LetterTile("e")
    m = LetterTile("m")
    a = LetterTile("a")
    o = LetterTile("o")
    z = LetterTile("z")
    x = LetterTile("x")

    board.set_tile(1, 1, d)
    board.set_tile(2, 1, e)
    board.set_tile(3, 1, m)
    board.set_tile(3, 2, m)
    board.set_tile(3, 3, m)
    board.set_tile(3, 4, a)
    board.set_tile(4, 1, o)
    board.set_tile(2, 2, o)
    board.set_tile(4, 2, z)
    board.set_tile(4, 4, z)
    board.set_tile(10, 3, z)
    board.set_tile(10, 4, z)
    board.set_tile(10, 5, z)
    board.set_tile(10, 6, z)
    board.set_tile(10, 7, z)
    board.set_tile(10, 10, z)
    board.set_tile(9, 10, a)
    board.set_tile(9, 9, m)
    board.set_tile(1, 10, x)
    board.set_tile(2, 10, x)
    board.set_tile(3, 10, x)
    board.set_tile(4, 10, x)
    board.set_tile(5, 10, x)

    board.print_board()

    print("There are {} letters placed on the board.".format(board.letters_placed()))

    print("=== Words ===")
    for word in board.get_words():
        print(word)

    print("=== Top Scoring Words ===")
    for word in board.top_scoring_words():
        print(word)
