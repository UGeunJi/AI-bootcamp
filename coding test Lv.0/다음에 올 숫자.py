등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

- 제한사항
2 < common의 길이 < 1,000
-1,000 < common의 원소 < 2,000
등차수열 혹은 등비수열이 아닌 경우는 없습니다.
공비가 0인 경우는 없습니다.

 common	        result
[1, 2, 3, 4]	  5
[2, 4, 8]	      16


def solution(common):
    answer = 0
    
    if common[2] == common[0] + ((common[1] - common[0]) * 2):
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1] // common[0])
    
    return answer
