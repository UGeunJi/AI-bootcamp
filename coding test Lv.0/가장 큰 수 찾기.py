정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    answer = []
    a = max(array)
    b = array.index(max(array))
    answer.append(a)
    answer.append(b)
    return answer
