# from parser import *

def get_grammar_info(filename):
    _two_symbols_rules = {}
    _lexicon_rules = {}
    _lexicon = {}

    with open(filename, 'r') as f:
        _grammar_lines, _lexicon_lines  = f.read().split("\n\n")

        _grammar_lines = _grammar_lines.split("\n")
        for _line in _grammar_lines:
            LHS, RHS = _line.split("->")
            LHS = LHS.strip()
            RHS = RHS.strip().split(" ")
            if len(RHS) == 2:
                _two_symbols_rules.setdefault(LHS, [])
                if RHS not in _two_symbols_rules[LHS]:
                    _two_symbols_rules[LHS].append(RHS)
            elif len(RHS) == 1:
                _lexicon_rules.setdefault(RHS[0], [])
                if RHS not in _lexicon_rules[RHS[0]]:
                    _lexicon_rules[RHS[0]].append(LHS)
            else:
                print("ERROR: Grammar must be in Chomsky normal form")

        _lexicon_lines = _lexicon_lines.split("\n")
        for _line in _lexicon_lines:
            LHS, RHS = _line.split("->")
            LHS = LHS.strip()
            RHS = RHS.strip()
            _lexicon.setdefault(RHS, [])
            if LHS not in _lexicon[RHS]:
                _lexicon[RHS].append(LHS)

    return _two_symbols_rules, _lexicon_rules, _lexicon

def read_input():
    pass

if __name__ == "__main__":
    """
    1. load & save grammar.txt
    2. load input.txt
        make seq. of terminals from input string
    3. CKY parser
        use seq.of terminals && CFG
        generate used_grammar.txt
    4. generate output.txt(parse tree)
    """

    two_symbols_rules, lexicon_rules, lexicon = get_grammar_info(filename = "grammar.txt")
    read_input()

