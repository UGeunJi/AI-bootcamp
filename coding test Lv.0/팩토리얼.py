i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

i! ≤ n

def solution(n):
    answer = 0
    if n == 1:
        answer = 1
    elif 2 <= n <= 5:
        answer = 2
    elif 6 <= n <= 23:
        answer = 3
    elif 24 <= n <= 119:
        answer = 4
    elif 120 <= n <= 719:
        answer = 5
    elif 720 <= n <= 5039:
        answer = 6
    elif 5040 <= n <= 40319:
        answer = 7
    elif 40320 <= n <= 362879:
        answer = 8
    elif 362880 <= n <= 3628799:
        answer = 9
    elif n == 3628800:
        answer = 10
        
    return answer
