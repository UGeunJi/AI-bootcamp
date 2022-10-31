문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i].islower() == True:
            answer += my_string[i].upper()
        elif my_string[i].isupper() == True:
            answer += my_string[i].lower()
    return answer
