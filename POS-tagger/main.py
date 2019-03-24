from trie import Trie
# from tabular_parse import TabularParse


def make_morph_dict(filename):
    """
    1. grammar.txt를 읽어온다. grammar.txt의 구조는 다음과 같다.
        단어 형태소/품사+형태소/품사+... 
    2. grammar.txt의 내용을 형태소를 key로 하고 POS를 value로 하는 dictionary에 저장한다.
    """
    f = open(filename)
    morph_pos_dict = {}
    for line in f.readlines():
        word, word_info = line.rstrip().split(' ')
        morph_list = word_info.split('+')
        for elem in morph_list:
            morph, pos = elem.split('/')
            morph_pos_dict.setdefault(morph, [])
            if pos not in morph_pos_dict[morph]:
                morph_pos_dict[morph].append(pos)
    return morph_pos_dict
  

def make_morph_connect_rule(filename):
    """
    1. grammar.txt를 읽어온다. grammar.txt의 구조는 다음과 같다.
        단어 형태소/품사+형태소/품사+... 
    2. 각 단어마다 형태소의 좌우접속정보를 읽어와 저장한다.
    3. 좌우접속정보를 저장하는 list를 반환한다.
    """
    f = open(filename)
    morph_connect_rule = []
    for line in f.readlines():
        _ , word_info = line.rstrip().split(' ')
        morph_list = word_info.split('+')
        pos_list = []
        for elem in morph_list:
            _, pos = elem.split('/')
            pos_list.append(pos)
        for i in range(len(pos_list)-1):
            connect_rule = (pos_list[i], pos_list[i+1])
            if connect_rule not in morph_connect_rule:
                morph_connect_rule.append((pos_list[i], pos_list[i+1]))
    return morph_connect_rule


if __name__ == "__main__" :
    """
    1. 사전 만들기
    - morph_pos_dict는 형태소를 key, 품사를 value로 하는 python dictionary이다.
    - morph_pos_dict를 돌면서 형태소 사전(Trie 구조)에 node를 추가한다.
    """
    morph_pos_dict = make_morph_dict("grammar.txt")
    trie = Trie()

    """
    2. 형태소 분석(Tabular parsing)
    """
    morph_connect_rule = make_morph_connect_rule("grammar.txt")
    print(morph_connect_rule)
    # TabularParse(trie, morph_connect_rule)


