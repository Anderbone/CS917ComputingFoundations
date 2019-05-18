import random

class linkedListNode:
    """
    A linked list node represents one element in the linked-list chain.
    In a singly linked-list it should have information about itself (the data)
    and how to find the next node in the list (next). The types of these should
    correspond accordingly.

    HINT: You can store an instance of an object inside another object, even if
    they are the same type (but you should be very careful when doing this
    with init funtions, you can end up calling the constructor infinitely via recursion)
    """
    def __init__(self,value):
        self.value = value
        self.next = None

    """ 
    set nextNode to be the node that this node points to
    """
    def setNext(self, nextNode):
        self.next = nextNode

    """
    Return the value stored at this node
    """
    def getValue(self):
        return self.value

    """
    Update the value stored at this node
    """
    def setValue(self,value):
        self.value = value

    """
    Return the next node in the linked-list that this
    node points to
    """

    def getNext(self):
        return self.next

class linkedList:
    """
    The linked list is the external facing component of the data structure.
    In should contain a selection of items:
    head - This is the first node in the linked-list
    tail - This is the last node in the linked-list

    Operations on a linked list tend to consist of one of two approaches:
    Modifying the value of a node - this requires you to find a node and update its
    value

    Modifying the position of a node - this requires you to find a node (or the
    preceeding node, and change its pointer to the 'next' node to either skip
    or refer to a new node)
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    """
    Set the value at postion <index> to be <value>.
    Hint: You will need to find the node that stores this value first
    """
    def set(self,index,value):
        if(index > self.size()):
            print('Error')
        count = 0
        target = self.head
        while count < index:
            target = target.getNext()
            count += 1
        target.setValue(value)

    """
    Return the value at postion <index>.
    Hint: You will need to find the node that stores this value first
    """
    def get(self,index):
        pass

    """
    Insert this value at poisition <index>
    Hint: You will need to find the node that preceeds the node already at this
    point, make it point at our new node and make our new node point at the old
    node at this index.
    """
    def insert(self,index,value):
        pass

    """
    Insert this value at position <index>
    Hint: You will need to find the node that preceeds the node at this index, 
    and make it point at the node after this index, skipping the node we
    are deleting entirely. 
    """
    def delete(self,index):
        pass

    """
    Return the number of nodes in our linked-list
    """
    def size(self):
        pass

    """
    Add a node with <value> to the end of our linked-list, and update the tail
    accordingly.
    Hint: What happens if the linked-list is empty?
    """
    def append(self,value):
        pass

def generateRandomList(length):
    result = []

    for i in range(0,length):
        result.append(random.randint(0,10000))
    return result

def generateRandomLinkedList(length):
    result = linkedList()

    for i in range(0,length):
        result.append(random.randint(0,10000))
    return result

def main():
    pass

if __name__ == "__main__":
    main()