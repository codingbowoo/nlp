class TrieNode(object):
    def __init__(self, entry, pos=list(), can_leaf=False):
        # check if the entry is string type
        try:
            assert isinstance(entry, str)
            self.entry = entry
        except:
            raise TypeError("entry attribute is not string type")
        self.children = {}
        self.can_leaf = can_leaf
        self.pos = pos

    def __repr__(self):
        return repr(self.children if self.children else "Leaf")

    def __eq__(self, char):
        assert len(char) == 1, "Invalid character"
        return self.entry == char

    def add(self, morph=None, pos=None):
        node = self.children.setdefault(morph[0], TrieNode(morph[0]))
        if len(morph) == 1:
            node.can_leaf = True
            if pos not in node.pos:
                node.pos.append(pos)
        else:
            node.add(morph[1:], pos)

    
class Trie(object):
    """
    Python implementation of Trie data structure
    """
    def __init__(self):
        self.trie = {}

    def __repr__(self):
        return repr(self.trie)

    def add(self, morph=None, pos=None):
        node = self.trie.setdefault(morph[0], TrieNode(morph[0]))
        if len(morph) == 1:
            node.can_leaf = True
            if pos not in node.pos:
                node.pos.append(pos)
        else:
            node.add(morph[1:], pos)


