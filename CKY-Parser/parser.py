from pprint import * 

class Node(object):
    def __init__(self, idx=1, symbol=None, left=None, down=None):
        self.idx = idx
        self.symbol = symbol
        self.left = left
        self.down = down

    def __repr__(self):
        return "("+str(self.idx)+")"+self.symbol

class Parser(object):
    def __init__(self, _two_symbols_rules=None, _lexicon_rules=None, _lexicon=None):
        self.parse_table = None
        self._two_symbols_rules = _two_symbols_rules
        self._lexicon_rules = _lexicon_rules
        self._lexicon = _lexicon
        self.f_grammar = open("used_grammar.txt", "a+")
        self.f_output = open("output.txt", "a+")
        self.idx = 1

    def write_used_grammar(self, used_grammar=[]):
        pass

    def init_parse_table(self, input):
        self.idx = 1
        length = len(input)
        self.parse_table = [[[] for j in range(length+1)] for i in range(length)]

        for i in range(length):
            # 1. initialize using _lexicon
            token = input[i]
            for elem in self._lexicon[token]:
                self.parse_table[i][i+1].append(Node(idx=self.idx, symbol=elem))
                self.idx += 1
             
                # 2. initialize using _lexicon_rules
                if elem in self._lexicon_rules:
                    self.parse_table[i][i+1].append(Node(idx=self.idx, symbol=self._lexicon_rules[elem][0]))
                    self.idx += 1


    def fill_table(self, left_nodes=[], down_nodes=[]):
        _list = []

        # make new rule
        if len(left_nodes)*len(down_nodes) == 0 : return []
        for left_node in left_nodes:
            for down_node in down_nodes:
                new_rule = []
                new_rule.append(left_node.symbol)
                new_rule.append(down_node.symbol)
                
                # check grammar using _two_symbols_rules
                for rule in self._two_symbols_rules.items():
                    if new_rule in rule[1]:
                        _list.append(Node(idx=self.idx, symbol=rule[0], left=left_node, down=down_node))
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


        print(sentence)
        
        pprint(self.parse_table)


