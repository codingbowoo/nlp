1. 사용 언어: Python 3.7.2 
2. 프로그램 실행 방법
/*
 TODO: 프로그램 실행 방법 추가하기
 */

3. 각 파일에 대한 설명
[1] manual tagging 시 표준국어대사전에 나온 품사를 기반으로 하였으며, 세종프로젝트의 일환인 46개 품사 태그를 사용했습니다.

[2] grammar.txt 작성시, 앞으로 tabular parsing은 음절 단위로 진행되기 때문에 manual parsing과는 별도의 tagging을 적용한 부분이 있습니다. 예시로, “노란” 이라는 어절은 원래 노랗/형용사VA+ㄴ/관형형전성어미ETM 이지만, 본 형태소분석기에서는 노란/형용사VA로 취급합니다. 
    - 다음은 본 형태소 분석기에서 예외적으로 사전에 추가한 내용입니다.
        - 그건 그것/NP+ㄴ/JX —> 그건/NP
        - 그럴 그렇/VA+ㄹ/ETM —> 그럴/MM
        - 관대함을 관대/XR+하/XSA+ㅁ/XSN+을/JKO —> 관대함/NNG+을/JKO
        - 자랑했지만 자랑/NNG+하/XSV+였/EP+지만/EC —> 자랑/NNG+했/EP+지만/EC
        - 너그러움에도 너그럽/VA+ㅁ/XSN+에/JKB+도/JX —> 너그러움/NNG+에/JKB+도/JX
        - 인정할 인정/NNG+하/XSV+ㄹ/ETM —> 인정/NNG+할/MM
        - 노란 노랗/VA+ㄴ/ETM —> 노란/VA

[3] dictionary_TRIE.jpg는 예문(5문장)의 사전 TRIE 구조를 보여준다. 
[4] /*
    TODO: POS_tagger.zip 설명 추가
    - dictionary 생성
    - tabular parsing
    */
