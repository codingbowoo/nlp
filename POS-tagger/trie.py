from types import StringType


class Node(object):
    # Node: basis of Trie
    def __init__(self, entry):
        # check if the entry is string type
        try:
            assert type(entry) is StringType
            self.entry = entry
        except:
            raise TypeError("entry attribute is not string type")
        self.child = None
        self.is_leaf = False
        self.sibling = []

    
class Trie():
    """
    Python implementation of Trie data structure
    """
    def __init__(self):
        pass

    def addNode(self, args):
        pass

    def insertWord(self, args):
        pass

    def findWord(self, args):
        pass

