1. 사용 언어: Python 3.7.2

2. 프로그램 실행 방법
- python3 main.py 명령어로 실행한다. (macOS 기준)

3. 각 파일에 대한 설명
a. main.py
    - grammar.txt와 input.txt를 불러온다.
    - grammar information (CNF rules, lexicon)을 저장한다.
        - _two_symbols_rules: exactly 2 non-terminal symbols on the RHS
        - _lexicon_rules: CNF with 1 terminal symbol
        - _lexicon: 사전 정보(pos, token)를 저장한다. 
b. parser.py
    - class Node
        - 트리 구조의 기본이 되는 Node 클래스이다.
    - class Parser
        - parse table을 생성하고 초기화한다.
        - 빈 table을 채울 때,  기존에 알려진 grammar information과 부합하는지 확인 과정을 거친다. 
        - 파싱을 마치면 dfs를 활용하여 tree를 print 해준다.

