문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

import math

def solution(my_str, n):
    answer = []
    
    for i in range(math.ceil(len(my_str) / n)):
            answer.append(''.join(my_str[i * n : n * (i + 1)]))
            

    return answer
