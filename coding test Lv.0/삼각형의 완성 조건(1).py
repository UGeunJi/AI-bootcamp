선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(sides):
    answer = 0
    sum = 0
    a = (max(sides))
         
    for i in range(len(sides)):
        sum += sides[i]
    
    if sum - a <= a:
        answer = 2
    else:
        answer = 1
    return answer
