import itertools
import collections
"""
For 917 assignment 2.
Author: Jiyu Yan.
Student ID:1851015

"""

def morsedict(morse):
    mdict = {'.-': 'A',
             '-...': 'B',
             '-.-.': 'C',
             '-..': 'D',
             '.': 'E',
             '..-.': 'F',
             '--.': 'G',
             '....': 'H',
             '..': 'I',
             '.---': 'J',
             '-.-': 'K',
             '.-..': 'L',
             '--': 'M',
             '-.': 'N',
             '---': 'O',
             '.--.': 'P',
             '--.-': 'Q',
             '.-.': 'R',
             '...': 'S',
             '-': 'T',
             '..-': 'U',
             '...-': 'V',
             '.--': 'W',
             '-..-': 'X',
             '-.--': 'Y',
             '--..': 'Z',
             '.----': '1',
             '..---': '2',
             '...--': '3',
             '....-': '4',
             '.....': '5',
             '-....': '6',
             '--...': '7',
             '---..': '8',
             '----.': '9',
             '-----': '0',
             }
    return mdict[morse]


def guesslist(num):
    guess = [''.join(i) for i in (itertools.product(['.', '-'], repeat=num))]
    return guess


def morse_all(test):
    xnum = len(test)
    guess = guesslist(xnum)
    all = []
    for replace in guess:
        possible = []
        i = 0
        for each in test:
            each = replace[i] + each[1:]
            possible.append(each)
            i += 1
        all.append(possible)
    return all


def inputdic(file):
    with open(file, 'r') as my_file:
        words = {every_line.rstrip().upper() for every_line in my_file}
        return words


def morseDecode(inputStringList):
    if inputStringList == []:
        return None
    word = []
    for i in inputStringList:
        word.append(morsedict(i))
    return ''.join(word)


def morsePartialDecode(inputStringList):
    dicwords = inputdic('./dictionary.txt')
    allpossible = morse_all(inputStringList)
    ans = []
    for i in allpossible:
        word = morseDecode(i)
        if word in dicwords:
            ans.append(word)
    return ans


class Maze:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.information = collections.defaultdict(lambda: '*')

    def addCoordinate(self, x, y, blockType):
        if x >= self.width:
            self.width = x+1
        if y >= self.height:
            self.height = y+1
        block = ' ' if blockType == 0 else '*'
        self.information[x, y] = block

    def printMaze(self):
        maze = [['*'] * self.width for i in range(self.height)]
        for i in self.information:
            if self.information[i] == ' ':
                maze[i[1]][i[0]] = self.information[i]

        for i in maze:
            print('|'.join(i))

    def manDistance(self,x1 ,y1, x2, y2):
        mdistance = abs(x1-x2) + abs(y1-y2)
        return mdistance

    def findRoute(self, x1, y1, x2, y2):

        openset = set()
        closedset = set()
        parent = {}
        route = []
        g_node = {}

        def f_node(node):
            fvalue = g_node[node] + self.manDistance(node[0], node[1], x2, y2)
            return fvalue

        def min_f(set):
            fmin = 1000000
            for each in set:
                f = f_node(each)
                if f < fmin:
                    fmin = f
                    x = each[0]
                    y = each[1]
            return x, y

        def reRoute(node):
            route.append(node)
            if node == (x1, y1):
                route.reverse()
                return route
            reRoute(parent[node])

        openset.add((x1, y1))
        g_node[x1, y1] = 0
        while len(openset) is not 0:
            current = min_f(openset)
            if current == (x2, y2):
                reRoute(current)
            openset.remove(current)
            closedset.add(current)
            temp = set()
            if self.information[current[0], current[1]+1] == ' ':
                temp.add((current[0], current[1]+1))
            if self.information[current[0], current[1]-1] == ' ':
                temp.add((current[0], current[1] - 1))
            if self.information[current[0]+1, current[1]] == ' ':
                temp.add((current[0]+1, current[1]))
            if self.information[current[0]-1, current[1]] == ' ':
                temp.add((current[0]-1, current[1]))

            for eachNeighbor in temp:
                if eachNeighbor in closedset:
                    continue
                new_g = 1 + g_node[current]

                if eachNeighbor not in openset:
                    openset.add(eachNeighbor)
                elif g_node[eachNeighbor] <= new_g:
                    continue
                g_node[eachNeighbor] = new_g
                parent[eachNeighbor] = current
        return route

def morseCodeTest():

    hello = ['....', '.', '.-..', '.-..', '---']
    print(morseDecode(hello))


def partialMorseCodeTest():

    test = ['x', 'x', 'x..', 'x']
    print(morsePartialDecode(test))

    dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    print(morsePartialDecode(dance))


def mazeTest():

    myMaze = Maze()
    myMaze.addCoordinate(1, 0, 0)
    myMaze.addCoordinate(1, 1, 0)
    myMaze.addCoordinate(7, 1, 0)
    myMaze.addCoordinate(1, 2, 0)
    myMaze.addCoordinate(2, 2, 0)
    myMaze.addCoordinate(3, 2, 0)
    myMaze.addCoordinate(4, 2, 0)
    myMaze.addCoordinate(6, 2, 0)
    myMaze.addCoordinate(7, 2, 0)
    myMaze.addCoordinate(4, 3, 0)
    myMaze.addCoordinate(7, 3, 0)
    myMaze.addCoordinate(4, 4, 0)
    myMaze.addCoordinate(7, 4, 0)
    myMaze.addCoordinate(3, 5, 0)
    myMaze.addCoordinate(4, 5, 0)
    myMaze.addCoordinate(7, 5, 0)
    myMaze.addCoordinate(1, 6, 0)
    myMaze.addCoordinate(2, 6, 0)
    myMaze.addCoordinate(3, 6, 0)
    myMaze.addCoordinate(4, 6, 0)
    myMaze.addCoordinate(5, 6, 0)
    myMaze.addCoordinate(6, 6, 0)
    myMaze.addCoordinate(7, 6, 0)
    myMaze.addCoordinate(5, 7, 0)

    myMaze.addCoordinate(0, 0, 0)
    myMaze.addCoordinate(3, 4, 0)
    myMaze.addCoordinate(2, 4, 0)
    myMaze.addCoordinate(1, 4, 0)
    myMaze.addCoordinate(0, 4, 0)
    myMaze.addCoordinate(0, 5, 0)

    myMaze.printMaze()
    ans = myMaze.findRoute(0, 0, 0, 5)
    print(ans)
    ans = myMaze.findRoute(1,0,5,7)
    print(ans)
    ans = myMaze.findRoute(1,1,7,6)
    print(ans)
    ans = myMaze.findRoute(1,1,6,7)
    print(ans)

def main():
    morseCodeTest()
    partialMorseCodeTest()
    mazeTest()

if (__name__ == "__main__"):
    main()
