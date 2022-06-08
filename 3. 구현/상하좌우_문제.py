"""
1. N x N 정사각형 공간
2. 시작 좌표(1, 1)
3. 상, 하, 좌, 우로 이동
4. 정사각형을 벗어나는 움직임은 무시
"""

# N=5
# R -> R -> R -> U -> D -> D


N = int(input())  # 2차원 크기
directs = input().split()  # 방향
tourist = [0, 0]  # 여행자 위치

dx = [-1, 1]  # 위, 아래
dy = [-1, 1]  # 왼, 오

for dir in directs:
    if dir == 'U':
        if (tourist[0] - 1) < 0:
            continue
        tourist[0] -= 1
    if dir == 'D':
        if (tourist[0] + 1) >= N:
            continue
        tourist[0] += 1
    if dir == 'L':
        if (tourist[1] - 1) < 0:
            continue
        tourist[1] -= 1
    if dir == 'R':
        if (tourist[1] + 1) >= N:
            continue
        tourist[1] += 1

# 좌표체계와 현실좌표 차이를 위해 +1
tourist[0] += 1
tourist[1] += 1

print(tourist)

"""책 소스코드
N = int(input()) #2차원 크기
directs = input().split() #방향
tourist = [1, 1] #여행자 위치

# 왼, 오, 위, 아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for dir in directs:
  for i in range(len(move_types)):
    if dir == move_types[i]:
      nx = tourist[0] + dx[i]
      ny = tourist[1] + dy[i]

  if nx < 1 or nx > N or ny < 1 or ny > N:
    continue

  tourist[0] = nx
  tourist[1] = ny

print(tourist)
"""