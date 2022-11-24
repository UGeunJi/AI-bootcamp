프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다.
시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

def solution(chicken):
    answer = 0
    
    chi = 0
    cou = 0
    cou1 = 0
    cou2 = 0
    
    if chicken < 10:
        answer = 0
    else:
        while chicken >= 10:
            cou += chicken % 10
            chi += chicken // 10
            chicken //= 10
        
        cou += chicken
        
        while cou >= 10:
            cou1 += cou % 10
            chi += cou // 10
            cou //= 10
        
        cou1 += cou
        
        while cou1 >= 10:
            cou2 += cou1 % 10
            chi += cou1 // 10
            cou1 //= 10
        
        cou2 += cou1
        
    answer = chi
    return answer
