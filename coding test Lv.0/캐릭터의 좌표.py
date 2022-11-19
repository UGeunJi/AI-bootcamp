머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다.
예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다.
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다.
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

[0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

def solution(keyinput, board):
    answer = []
    a = [0, 0]
    
    board[0] /= 2
    board[1] /= 2
    board = list(map(int, board))   
    
    for i in keyinput:
        if i == 'left':
            if abs(a[0]) < board[0]:
                a[0] -= 1
            elif a[0] != -board[0]:
                a[0] -= 1
        elif i == 'right':
            if abs(a[0]) < board[0]:
                a[0] += 1
            elif a[0] != board[0]:
                a[0] += 1
        elif i == 'up':
            if abs(a[1]) < board[1]:
                a[1] += 1
            elif a[1] != board[1]:
                a[1] += 1
        elif i == 'down':
            if abs(a[1]) < board[1]:
                a[1] -= 1
            elif a[1] != -board[1]:
                a[1] -= 1
                
    answer = a
    return answer
