머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

def solution(price):
    answer = 0
    if price >= 500000:
        answer = price - (price / 5)
    elif 300000 <= price < 500000:
        answer = price - (price / 10)
    elif 100000 <= price < 300000:
        answer = price - (price / 20)
    else:
        answer = price
    return int(answer)
