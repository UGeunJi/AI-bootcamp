문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

import re

def solution(my_string):
    return sorted(list(map(int, re.findall(r'\d', my_string))))
