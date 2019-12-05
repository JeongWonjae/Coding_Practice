#2번 알고리즘- 더 킹 레이스

#체스판 돌위에 흑백하나씩 있을때
#누가 먼저 도착지에 도착하는가
#흰색돌은 항상 (1,1) 흑돌은 (n,n)에 위치
#도착지=코인은 (x,y)에 있음
#백돌이 먼저 움직임
#돌은 8가지 방향으로 움직일 수 있음
#이동횟수는 가로, 세로 좌표중 더 긴것이됨

#n은 x,y는 코인의 위치
def algo(n, x, y):
    if n-x>n-y: black=n-x
    else: black=n-y
    if x-1>y-1: white=x-1
    else: white=y-1

    if white==0 or white<black: print('White Win!')
    elif black==0 or black<white: print('Black Win!')

algo(5, 3, 4)
algo(3, 1, 1)

