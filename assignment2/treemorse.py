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
    nodelist = []

    def __init__(self, morselist):
        self.root = self.child = MorseTreeNode('')
        # p = self.root
        # n = len(morselist)
        # for i in range(n):
        #     for each in self.getchild():
        #         self.insert(each, morselist[i])

        for code in morselist:
            for each in self.getchild():
                self.insert(each, code)

    def DFSInOrder(self, node):
        leftChild = node.getLeftChild()
        if leftChild is not None:
            self.DFSInOrder(leftChild)
        # print(node.value)
        global nodelist
        nodelist.append(node)
        RightChild = node.getRightChild()
        if RightChild is not None:
            self.DFSInOrder(RightChild)

    def getchild(self):
        childlist = []
        self.DFSInOrder(self.root)
        global nodelist
        for p in nodelist:
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
        child.leftChild = MorseTreeNode(re.sub('x', '.', value))
        child.rightChild = MorseTreeNode(re.sub('x', '-', value))
        # self.child = [child.leftChild, child.rightChild]
