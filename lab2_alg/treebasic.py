
class BinaryTreeNode():

    def __init__(self,value):
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

    def setLeftChild(self,node):
        self.leftChild = node

    def setRightChild(self,node):
        self.rightChild = node

    def setValue(self,value):
        self.value = value

class BinaryTree():
    def __init__(self, rootValue):
        self.root = BinaryTreeNode(rootValue)

    def getRootNode(self):
        return self.root

    # def insertAtRoot(self,value):
    #     self.insert(self.root,value)

    def insertValue(self, value):
        self.insert(self.root, value)

    def insert(self, parent, value):
        if parent is None:
            return BinaryTreeNode(value)

        if value <= parent.value:
            parent.leftChild = self.insert(parent.getLeftChild(), value)
            return parent
        if value > parent.value:
            parent.rightChild = self.insert(parent.getRightChild(), value)
            return parent

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

def DFSInOrder(node):
    leftChild = node.getLeftChild()
    if leftChild is not None:
        DFSInOrder(leftChild)
    print(node.value)
    RightChild = node.getRightChild()
    if RightChild is not None:
        DFSInOrder(RightChild)



    # if node.getLeftChild() is not None:
    #     DFSInOrder(node.getLeftChild())
    # print(node.value)
    # if node.getRightChild() is not None:
    #     DFSInOrder(node.getRightChild())


def DFSPreOrder(node):
    print(node.value)
    if node.getLeftChild() is not None:
        DFSInOrder(node.getLeftChild())
    if node.getRightChild() is not None:
        DFSInOrder(node.getRightChild())
def DFSPostOrder(node):

    if node.getRightChild() is not None:
        DFSInOrder(node.getRightChild())
    if node.getLeftChild() is not None:
        DFSInOrder(node.getLeftChild())
    print(node.value)



def main():
    tree = BinaryTree(14)  # Create a tree with a root Node value of 14
    tree.insertValue(12)  # Inserts a node of value 12
    tree.insertValue(16)  # Insert a node of value 16
    tree.insertValue(18)  # Insert a node of value 18
    tree.insertValue(5)  # Insert a node of value 5
    tree.insertValue(21)  # Insert a node of value 21
    tree.insertValue(3)  # Insert a node of value 3

    print('---------')

    print("PreOrder")
    DFSPreOrder(tree.getRootNode())

    print('---------')

    print("InOrder")
    DFSInOrder(tree.getRootNode())

    print('---------')

    print ("PostOrder")
    DFSPostOrder(tree.getRootNode())

    print ('---------')

    print ("BFS")
    tree.treeBFS()

if __name__ == "__main__":
    main()