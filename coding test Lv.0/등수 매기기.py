영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다.
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.


score	                                                                           result
[[80, 70], [90, 50], [40, 70], [50, 80]]	                                  [1, 2, 4, 3]
[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]	  [4, 4, 6, 2, 2, 1, 7]


import numpy as np

def solution(score):
    answer = []
    su = []
    sor = []
    b = []
    
    score = np.array(score)
    su = np.sum(score, 1)
    
    for i in range(len(su)):
        b.append(su[i] / 2)
    
    sor = sorted(b, reverse = True)
    
    for j in b:
        answer.append(sor.index(j) + 1)
    
    return answer
