class Node(object):
    def __init__(self, symbol, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right

    def __repr__(self):
        return self.symbol

class ParseTree(object):
    def __init__(self):
        self.root = None

