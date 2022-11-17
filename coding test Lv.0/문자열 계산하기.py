my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

def solution(my_string):
    answer = 0
    
    numbers = my_string.split(' ')
    answer += int(numbers[0])
    
    for i in range(1, len(numbers), 2):
        if numbers[i] == '+':
            answer += int(numbers[i + 1])
        elif numbers[i] == '-':
            answer -= int(numbers[i + 1])
    return answer
