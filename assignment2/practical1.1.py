import itertools

import re


class MorseTreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    """
    These getter and setter methods are here to highlight
    the kinds of data you want to access or retrieve.
    """

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getValue(self):
        return self.value

    def setLeftChild(self, node):
        self.leftChild = node

    def setRightChild(self, node):
        self.rightChild = node

    def setValue(self, value):
        self.value = value

    def isLeaf(self):
        if self.leftChild and self.rightChild is None:
            return True
        else:
            return False


class MorseTree:

    def __init__(self, morselist):
        self.root = self.child = MorseTreeNode('')
        # p = self.root
        # n = len(morselist)
        # for i in range(n):
        #     for each in self.getchild.():
        #         self.insert(each, morselist[i])
        self.depth = 0
    # def binaryTreePaths(self, root):
    #
    #     self.ans = []
    #     if root == None:
    #         return self.ans
    #
    #     def dfs(root, path):
    #         if root and root.leftChild is None and root.rightChild is None:
    #             self.ans.append(path)
    #         elif root.leftChild:
    #             root.leftChild = dfs(root.leftChild, path + '->' + str(root.leftChild.value))
    #         elif root.rightChild:
    #             root.rightChild = dfs(root.rightChild, path + '->' + str(root.rightChild.value))
    #
    #     dfs(root, root.value)
    #     print(self.ans)
    #     return self.ans
    def DFSInOrder(self, node):
        leftChild = node.getLeftChild()
        if leftChild is not None:
            self.DFSInOrder(leftChild)
        print(node.value)
        self.nodelist.append(node)
        # nodelist.append(node)
        RightChild = node.getRightChild()
        if RightChild is not None:
            self.DFSInOrder(RightChild)

    def getchild(self):
        childlist = []
        self.DFSInOrder(self.root)
        print(len(self.nodelist))
        # nodelist
        for p in self.nodelist:
            if p.isLeaf() is True:
                childlist.append(p)
        return childlist

    # def insertValue(self, value):
    #     self.insert(self.root, value)

    # def insert(self, parent, value):
    #
    #     if 'x' in value:
    #         parent.leftChild = self.insert(parent.getLeftChild(), re.sub('x', '.', value))
    #         parent.rightChild = self.insert(parent.getRightChild(), re.sub('x', '-', value))
    #         return parent
    #     else:
    #         parent.leftChild = self.insert(parent.getLeftChild(), value)

    def insert(self, child, value):
        print('kong?'+ value)
        child.leftChild = MorseTreeNode(re.sub('x', '.', value))
        child.rightChild = MorseTreeNode(re.sub('x', '-', value))
        # self.child = [child.leftChild, child.rightChild]
        print(re.sub('x', '.', value))

    def treeBFS(self):
        queue = [self.root]
        BFS(queue)

def BFS(queue):
    if len(queue) == 0:
        return None

    node = queue.pop(0)
    if node.getLeftChild() is not None:
        queue.append(node.getLeftChild())
    if node.getRightChild() is not None:
        queue.append(node.getRightChild())
    print(node.value)
    BFS(queue)

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

def inputdic(file):
    with open(file, 'r') as my_file:
        words = {every_line.rstrip() for every_line in my_file}
        return words

def morseDecode(inputStringList):
	# """
	# This method should take a list of strings as input. Each string is equivalent to one letter
	# (i.e. one morse code string). The entire list of strings represents a word.
    #
	# This method should convert the strings from morse code into english, and return the word as a string.
    #
	# """
	# Please complete this method to perform the above described function
        word = []
        for i in inputStringList:
            word.append(morsedict(i))
        return ''.join(word)



def morsePartialDecode(inputStringList):
	"""
	This method should take a list of strings as input. Each string is equivalent to one letter
	(i.e. one morse code string). The entire list of strings represents a word.

	However, the first character of every morse code string is unknown (represented by an 'x' (lowercase))
	For example, if the word was originally TEST, then the morse code list string would normally be:
	['-','.','...','-']

	However, with the first characters missing, I would receive:
	['x','x','x..','x']

	With the x unknown, this word could be TEST, but it could also be EESE or ETSE or ETST or EEDT or other permutations.

	We define a valid words as one that exists within the dictionary file provided on the website, dictionary.txt
	When using this file, please always use the location './dictionary.txt' and place it in the same directory as
	the python script.

	This function should find and return a list of strings of all possible VALID words.
	"""

	dictionaryFileLoc = './dictionary.txt'
	# Please complete this method to perform the above described function
	dicwords = inputdic('./dictionary.txt')
	# print('gith' in dicwords)
	tree = MorseTree(inputStringList)
	tree.DFSInOrder(tree.root)
	tree.binaryTreePaths(tree.root)

class Maze:
	def __init__(self):
		"""
		Constructor - You may modify this, but please do not add any extra parameters
		"""

		pass

	def addCoordinate(self,x,y,blockType):
		"""
		Add information about a coordinate on the maze grid
		x is the x coordinate
		y is the y coordinate
		blockType should be 0 (for an open space) of 1 (for a wall)
		"""

		# Please complete this method to perform the above described function
		pass

	def printMaze(self):
		"""
		Print out an ascii representation of the maze.
		A * indicates a wall and a empty space indicates an open space in the maze
		"""

		# Please complete this method to perform the above described function
		pass

	def findRoute(self,x1,y1,x2,y2):
		"""
		This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
		It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
		in the order in which the coordinates must be followed
		If no route is found, return an empty list
		"""
		pass

def morseCodeTest():
        # """
        # This test program passes the morse code as a list of strings for the word
        # HELLO to the decode method. It should receive a string "HELLO" in return.
        # This is provided as a simple test example, but by no means covers all possibilities, and you should
        # fulfill the methods as described in their comments.
        # """
    hello = ['....','.','.-..','.-..','---']
    print(morseDecode(hello))


def partialMorseCodeTest():

	"""
	This test program passes the partial morse code as a list of strings
	to the morsePartialDecode method. This is provided as a simple test example, but by
	no means covers all possibilities, and you should fulfill the methods as described in their comments.
	"""




	# This is a partial representation of the word TEST, amongst other possible combinations
	test = ['x','x','x..','x']
	print(morsePartialDecode(test))

	# This is a partial representation of the word DANCE, amongst other possible combinations
	dance = ['x..','x-','x.','x.-.','x']
	print(morsePartialDecode(dance))

def mazeTest():
	"""
	This sets the open space coordinates for the example
	maze in the assignment.
	The remainder of coordinates within the max bounds of these specified coordinates
	are assumed to be walls
	"""
	myMaze = Maze()
	myMaze.addCoordinate(1,0,0)
	myMaze.addCoordinate(1,1,0)
	myMaze.addCoordinate(7,1,0)
	myMaze.addCoordinate(1,2,0)
	myMaze.addCoordinate(2,2,0)
	myMaze.addCoordinate(3,2,0)
	myMaze.addCoordinate(4,2,0)
	myMaze.addCoordinate(6,2,0)
	myMaze.addCoordinate(7,2,0)
	myMaze.addCoordinate(4,3,0)
	myMaze.addCoordinate(7,3,0)
	myMaze.addCoordinate(4,4,0)
	myMaze.addCoordinate(7,4,0)
	myMaze.addCoordinate(3,5,0)
	myMaze.addCoordinate(4,5,0)
	myMaze.addCoordinate(7,5,0)
	myMaze.addCoordinate(1,6,0)
	myMaze.addCoordinate(2,6,0)
	myMaze.addCoordinate(3,6,0)
	myMaze.addCoordinate(4,6,0)
	myMaze.addCoordinate(5,6,0)
	myMaze.addCoordinate(6,6,0)
	myMaze.addCoordinate(7,6,0)
	myMaze.addCoordinate(5,7,0)

def main():
	morseCodeTest()
	partialMorseCodeTest()
	mazeTest()

if(__name__ == "__main__"):
	main()