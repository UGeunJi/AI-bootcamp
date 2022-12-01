머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ babbling의 길이 ≤ 100
1 ≤ babbling[i]의 길이 ≤ 15
babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
문자열은 알파벳 소문자로만 이루어져 있습니다.


입출력 예
babbling	                                     result
["aya", "yee", "u", "maa", "wyeoo"]	             1
["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	     3


입출력 예 #1
["aya", "yee", "u", "maa", "wyeoo"]에서 발음할 수 있는 것은 "aya"뿐입니다. 따라서 1을 return합니다.

입출력 예 #2
["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]에서 발음할 수 있는 것은 "aya" + "ye" = "ayaye", "ye", "ye" + "ma" + "woo" = "yemawoo"로 3개입니다. 따라서 3을 return합니다.




def solution(babbling):
    answer = 0
    b = []
    c = []
    
    a = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(a)):
        for j in range(len(a)):
            b.append(a[i] + a[j])

    d = a + b

    for i in range(len(d)):
        for j in range(len(d)):
            c.append(d[i] + d[j])

    d = b + a

    for i in range(len(d)):
        for j in range(len(d)):
            c.append(d[i] + d[j])

    c = d + c                                    # 모든 경우 리스트 c에 저장

    s = ["mama", "woowoo", "yeye", "ayaaya"]

    for i in range(len(s)):
        for j in range(len(c)):
            if s[i] in c[j]:
                c[j] = '0'                       # 연속되는 경우 삭제

    for i in range(len(a)):
        for j in range(len(c)):
            count = c[j].count(a[i])
            if count >= 2:
                c[j] = '0'                       # 1번 이상 쓰인 경우 삭제
                
    c = set(c)
    
    for i in range(len(babbling)):
        if babbling[i] in c:
            answer += 1
            
    return answer
