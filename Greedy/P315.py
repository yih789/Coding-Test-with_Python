# 조합
from itertools import combinations

# 볼링공 갯수 # 공의 최대 무게
N, M = map(int, input().split())

# 공의 무게 리스트
balls = list(map(int, input().split()))

# n개의 공 중 2개를 순서 없이 중복 없이 뽑는 경우
cases = list(combinations(range(len(balls)), 2))

# 그 중에서 무게가 같은 경우 제외
exclude_list = []

for i in range(len(cases)):
    a, b = cases[i]
    if balls[a] == balls[b]:
        exclude_list.append((a, b))
for exclude in exclude_list:
    if exclude in cases:
        cases.remove(exclude)

print(len(cases))