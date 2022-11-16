소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다.
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    
    if n == 2:
        answer.append(2)
    else:
        for i in range(2, n):
            while i < n:
                if n % i == 0:
                    break
                else:
                    answer.append(n)
                break
            break                               # n이 소수 한 개(자신)로 나눠질 때

        for i in range(2, n):
            if n % i == 0 and i <= (n // 2):
                answer.append(i)                # 이제 이게 소수이기만 하면 된다

        for i in range(2, n):                   # 합성수 제거
            for j in range(2, n):
                if i * j in answer:
                    answer.remove(i * j)
    return answer
