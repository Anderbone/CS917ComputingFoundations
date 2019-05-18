import time


class TrieTree(object):

  def __init__(self):
    self.tree = {}

  def add(self, word):
    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        tree[char] = {}
        tree = tree[char]

    tree['exist'] = True

  def search(self, word):
    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        return False

    if "exist" in tree and tree["exist"] == True:
      return True
    else:
      return False


tree = TrieTree()
# tree.add("abc")
# tree.add("bcd")
# print(tree.tree)
# # Print {'a': {'b': {'c': {'exist': True}}}, 'b': {'c': {'d': {'exist': True}}}}
# print(tree.search("ab"))
# # Print False
# print(tree.search("abc"))
# # Print True
# print(tree.search("abcd"))
# Print False
time1 = time.time()
with open('linux.words', 'r') as f:
    for word in f:
        tree.add(str(word))

time2 = time.time()
print('trie cost'+str(time2 - time1))

with open('linux.words', 'r') as f:
    mylist = []
    for word in f:
        mylist.append(str(word))
time3 = time.time()
print('list cost'+str(time3 - time2))
