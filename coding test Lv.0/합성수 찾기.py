약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = 0
    l = []
    
    for k in range(1, n + 1):
        l.append(k)
        
    for i in range(1, len(l)):
        if l[i] % 2 == 0 or l[i] % 3 == 0 or l[i] % 5 == 0 or l[i] % 7 == 0:
            if l[i] == 2 or l[i] == 3 or l[i] == 5 or l[i] == 7:
                continue
            answer += 1
            
    
    return answer
