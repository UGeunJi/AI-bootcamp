정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    answer = [numbers[i] * 2 for i in range(len(numbers))]
    return answer
