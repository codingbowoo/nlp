from pprint import * 

class Node(object):
    def __init__(self, idx=1, symbol=None, left=None, down=None, child=None):
        self.idx = idx
        self.symbol = symbol
        self.left = left
        self.down = down
        self.child = child

    def __repr__(self):
        return "("+str(self.idx)+")"+self.symbol

class Parser(object):
    def __init__(self, _two_symbols_rules=None, _lexicon_rules=None, _lexicon=None):
        self.parse_table = None
        self._two_symbols_rules = _two_symbols_rules
        self._lexicon_rules = _lexicon_rules
        self._lexicon = _lexicon
        self.f_grammar = open("used_grammar.txt", "w")
        self.f_output = open("output.txt", "w")
        self.idx = 1


    def init_parse_table(self, input):
        self.idx = 1
        length = len(input)
        self.parse_table = [[[] for j in range(length+1)] for i in range(length)]

        for i in range(length):
            # 1. initialize using _lexicon
            token = input[i]
            for elem in self._lexicon[token]:
                base_node = Node(self.idx, symbol=token)
                self.parse_table[i][i+1].append(base_node)
                self.f_grammar.write(str(base_node.idx) + " (" + elem + ", " + token + ")"+"\n")
                self.idx += 1
             
                # 2. initialize using _lexicon_rules
                if elem in self._lexicon_rules:
                    new_node = Node(idx=self.idx, symbol=self._lexicon_rules[elem][0], child=base_node)
                    self.parse_table[i][i+1].append(new_node)
                    self.f_grammar.write(str(new_node.idx) + " (" + new_node.symbol + ", " 
                        + "(" + str(new_node.child.idx)+")"
                        +")"+"\n")
                    self.idx += 1


    def fill_table(self, left_nodes=[], down_nodes=[]):
        _list = []

        # make new rule
        for left_node in left_nodes:
            for down_node in down_nodes:
                new_rule = []
                new_rule.append(left_node.symbol)
                new_rule.append(down_node.symbol)
                
                # check grammar using _two_symbols_rules
                for rule in self._two_symbols_rules.items():
                    if new_rule in rule[1]:
                        new_node = Node(idx=self.idx, symbol=rule[0], left=left_node, down=down_node)
                        _list.append(new_node)
                        self.f_grammar.write(str(new_node.idx) + " (" + new_node.symbol + ", " 
                        + "(" + str(new_node.left.idx)+", "+str(new_node.down.idx)+")"+")"
                        +")"+"\n")
     
                        
                        self.idx += 1
        return _list
                        
        

    def parse(self, sentence=[]):
        # initialize using _lexicon and _lexicon_rules
        self.init_parse_table(input=sentence)

        # fill parse_table; parse_table[i][j] = parse_table[i][k] + parse_table[k][j]
        for j in range(2, len(sentence)+1):
            for i in range(j-2, -1, -1):
                for k in range(j-1, i, -1):
                    if i >= j : continue
                    else:
                        self.parse_table[i][j] += self.fill_table(self.parse_table[i][k], self.parse_table[k][j])
        self.print_tree(len(sentence))


    def dfs(self, node=None, _visited=[], _output=""):
        if node.idx not in _visited:
            _visited.append(node.idx)
            _output += "(" + node.symbol + " "
            if node.left == None and node.down == None:
                if node.child != None :
                    _output += node.child.symbol
                _output += ")"
                return _visited, _output
            if node.left.idx not in _visited:
                _visited, _output = self.dfs(node=node.left, _visited=_visited, _output=_output)
            if node.down.idx not in _visited:
                _visited, _output = self.dfs(node=node.down, _visited=_visited, _output=_output)
            _output += ")"
        return _visited, _output


    def print_tree(self, input_len):
        roots = [node for node in self.parse_table[0][input_len] if node.symbol=="S"]
        for root in roots:
            visited, final_output = self.dfs(node=root, _visited=[], _output="")
            self.f_output.write(final_output+"\n")
        self.f_output.write("\n")
        self.f_grammar.write("\n")


