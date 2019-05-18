class BinaryTreeNode():

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


class BinaryTree():
    def __init__(self, rootValue):
        self.root = BinaryTreeNode(rootValue)

    def getRootNode(self):
        return self.root

    def insertValue(self, value):
        self.insert(self.root, value)

    def insert(self, parent, value):
        if (parent is None):
            return BinaryTreeNode(value)

        if (value <= parent.value):
            parent.leftChild = self.insert(parent.getLeftChild(), value)
            return parent

        if (value > parent.value):
            parent.rightChild = self.insert(parent.getRightChild(), value)
            return parent

    def treeBFS(self):
        queue = [self.root]
        BFS(queue)


def BFS(queue):
    # Using a list as a makeshift queue - there are more suitable data structures for this

    if len(queue) == 0:
        return None

    node = queue.pop(0)

    if (node.getLeftChild() is not None):
        queue.append(node.getLeftChild())

    if (node.getRightChild() is not None):
        queue.append(node.getRightChild())

    print(node.value)

    BFS(queue)


def DFSInOrder(node):
    leftChild = node.getLeftChild()
    if (leftChild is not None):
        DFSInOrder(leftChild)

    print(node.getValue())

    rightChild = node.getRightChild()
    if (rightChild is not None):
        DFSInOrder(rightChild)


def DFSPreOrder(node):
    print(node.getValue())

    leftChild = node.getLeftChild()
    if (leftChild is not None):
        DFSPreOrder(leftChild)

    rightChild = node.getRightChild()
    if (rightChild is not None):
        DFSPreOrder(rightChild)


def DFSPostOrder(node):
    leftChild = node.getLeftChild()
    if (leftChild is not None):
        DFSPostOrder(leftChild)

    rightChild = node.getRightChild()
    if (rightChild is not None):
        DFSPostOrder(rightChild)

    print(node.getValue())


def main():
    tree = BinaryTree(14)  # Create a tree with a root Node value of 14
    tree.insertValue(12)  # Inserts a node of value 12
    tree.insertValue(16)  # Insert a node of value 16
    tree.insertValue(18)  # Insert a node of value 18
    tree.insertValue(5)  # Insert a node of value 5
    tree.insertValue(21)  # Insert a node of value 21
    tree.insertValue(3)  # Insert a node of value 3

    DFSPreOrder(tree.getRootNode())


    DFSInOrder(tree.getRootNode())


    DFSPostOrder(tree.getRootNode())

    tree.treeBFS()


if __name__ == "__main__":
    main()