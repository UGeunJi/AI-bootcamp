첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

import fractions

def solution(denum1, num1, denum2, num2):
    answer = []
    if num1 != num2:
        s1 = denum1 * num2
        s2 = denum2 * num1
        m1 = num1 * num2
    else:
        s1 = denum1 + denum2
        s2 = 0
        m1 = num1
        
    s3 = s1 + s2
    a = fractions.Fraction(s3, m1)
    b = a.numerator
    c = a.denominator
    
    answer.append(b)
    answer.append(c)
    return answer
