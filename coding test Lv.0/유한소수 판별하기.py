소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다.
분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

def solution(a, b):
    answer = 0
    l = []
    q = []
    
    if a == b:
        answer = 1
    else:    
        for i in range(1, b):
            if a % i == 0 and b % i == 0:
                l.append(i)

        b = b // int(max(l))                    # b의 약수 중 가장 큰 값으로 b를 나눈 값 = 기약 분수의 분모

        if b == 2:
            q.append(2)
        else:
            for j in range(2, b):
                while j < b:
                    if b % j == 0:
                        break
                    else:
                        q.append(b)
                    break
                break                           # n이 소수 한 개(자신)로 나눠질 때

        for k in range(2, b):
            if b % k == 0 and k <= (b // 2):
                q.append(k)                     # 이제 이게 소수이기만 하면 된다

        for x in range(2, b):                   # 합성수 제거
            for y in range(2, b):
                if x * y in q:
                    q.remove(x * y)             # list l에 b의 소수만 있음

        for z in q:                             # 2나 5가 아닌 다른 수가 있으면 2로 반환
            if z == 2 and 3 not in q:
                answer = 1
            elif z == 5 and 3 not in q:
                answer = 1
            elif z == 2 and z == 5 and 3 not in q:
                answer = 1
            else:
                answer = 2
        
    return answer
