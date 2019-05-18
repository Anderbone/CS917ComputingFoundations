import itertools
import collections


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
        """
        This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
        It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
        in the order in which the coordinates must be followed
        If no route is found, return an empty list
        """
        # if self.information[x1, y1] == '*' or self.information[x2, y2] == '*':
        #     return []
        # store the father parent node
        openset = set()
        # print(openset)
        closedset = set()
        parent = {}
        route = []
        # current = (x1, y1)
        # g_node = collections.defaultdict(lambda: 100000)
        g_node = {}

        def f_node(node):
            fvalue = g_node[node] + self.manDistance(node[0], node[1], x2, y2)
            return fvalue

        def min_f(set):
            # x = 0
            # y = 0
            fmin = 1000000
            for each in set:
                # print(each)
                f = f_node(each)
                if f < fmin:
                    fmin = f
                    x = each[0]
                    y = each[1]
            return x, y
                # , fmin

        def reRoute(node):
            route.append(node)
            # print(route)
            if node == (x1, y1):
                route.reverse()
                # print(route)
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
                # temp[current[0], current[1]+1] = current
                temp.add((current[0], current[1]+1))
            if self.information[current[0], current[1]-1] == ' ':
                # temp[current[0], current[1]-1] = current
                temp.add((current[0], current[1] - 1))
            if self.information[current[0]+1, current[1]] == ' ':
                # temp[current[0]+1, current[1]] = current
                temp.add((current[0]+1, current[1]))
            if self.information[current[0]-1, current[1]] == ' ':
                # temp[current[0]-1, current[1]] = current
                temp.add((current[0]-1, current[1]))

            for eachNeighbor in temp:
                if eachNeighbor in closedset:
                    continue
                new_g = 1 + g_node[current]
                # if eachNeighbor not in openset:
                #     openset.add(eachNeighbor)
                #     parent[eachNeighbor] = current
                #     g_node[eachNeighbor] = new_g
                # else:
                #     # already in openset and new g socre is smaller.
                #     if g_node[eachNeighbor] > new_g:
                #         g_node[eachNeighbor] = new_g
                #     parent[eachNeighbor] = current
                if eachNeighbor not in openset:
                    openset.add(eachNeighbor)
                elif g_node[eachNeighbor] <= new_g:
                    continue
                g_node[eachNeighbor] = new_g
                parent[eachNeighbor] = current


        # print('after')
        # print(route)
        return route
        # openset.update(temp)
        # openset.remove((x1,y1))

        # compute the distance, choose the least distance one
        # for current in openset:
        #
        # # route.update(temp)
        # # print(route)
        # print(openset)









def morseCodeTest():
    """
    This test program passes the morse code as a list of strings for the word
    HELLO to the decode method. It should receive a string "HELLO" in return.
    This is provided as a simple test example, but by no means covers all possibilities, and you should
    fulfill the methods as described in their comments.
    """

    hello = ['....', '.', '.-..', '.-..', '---']
    print(morseDecode(hello))


def partialMorseCodeTest():
    """
    This test program passes the partial morse code as a list of strings
    to the morsePartialDecode method. This is provided as a simple test example, but by
    no means covers all possibilities, and you should fulfill the methods as described in their comments.
    """

    # This is a partial representation of the word TEST, amongst other possible combinations
    test = ['x', 'x', 'x..', 'x']
    print(morsePartialDecode(test))

    # This is a partial representation of the word DANCE, amongst other possible combinations
    dance = ['x..', 'x-', 'x.', 'x.-.', 'x']
    print(morsePartialDecode(dance))


def mazeTest():
    """
    This sets the open space coordinates for the example
    maze in the assignment.
    The remainder of coordinates within the max bounds of these specified coordinates
    are assumed to be walls
    """
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
    # ans = myMaze.findRoute(1, 0, 0, 5)
    print(ans)

    # myMaze.addCoordinate(9, 9, 0)
    # myMaze.addCoordinate(10, 1, 0)
    ans = myMaze.findRoute(1,0,5,7)
    print(ans)
    ans = myMaze.findRoute(1,1,7,6)
    print(ans)
    # print('no path')
    ans = myMaze.findRoute(1,1,6,7)
    print(ans)

    # myMaze.printMaze()





def main():
    morseCodeTest()
    partialMorseCodeTest()
    mazeTest()


if (__name__ == "__main__"):
    main()
