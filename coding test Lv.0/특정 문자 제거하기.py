문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string, letter):
    answer = ''
    m = list(my_string)
    for i in my_string:
        if letter in i:
            m.remove(i)
    m = ''.join(m)
    answer = m
    return answer
