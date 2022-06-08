"""
1. 8 x 8 평면
2. L자로만 이동 가능
  - 수평으로 두 칸 이동 후 수직으로 한 칸 이동
  - 수직으로 두 칸 이동 후 수평으로 한 칸 이동
3. 행은 1~8로 표현
4. 열은 a~h로 표현
5. 특정 위치에서 이동 가능한 경우의 수 출력
"""

# 특정 위치에서 이동 가능한 모든 경우의 수: 8
# 완전 탐색 문제와 비슷한 걸 알 수 있다.
# 상, 하, 좌, 우의 왼,오&위, 아래


data = input()
row = int(data[1])
col = (ord(data[0]) - ord('a')) + 1
count = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for step in steps:
    tmp_r = row + step[0]
    tmp_c = col + step[1]
    if tmp_r < 1 or tmp_r > 8 or tmp_c < 1 or tmp_c > 8:
        continue
    count += 1

print(count)