from itertools import permutations # 순열
from itertools import product # 중복순열
from itertools import combinations # 조합
from itertools import combinations_with_replacement # 중복조합
import copy # 깊은복사

N, M = map(int, input().split())

# N X M 연구소
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 바이러스 위치
virus = []

# 안전영역 크기
safety_list = []
safety = 0

# 재귀함수 # 상하좌우 인접
def dfs(graph, a, b):
    # 벽인지, 이동가능한지 확인
    if a < 0 or a > N-1 or b < 0 or b > M-1:
        return False
    if graph[a][b] == 1 or graph[a][b] == 3:
        return False

    # 방문처리
    graph[a][b] = 3

    # 상하좌우 방문
    dfs(graph, a-1, b)
    dfs(graph, a+1, b)
    dfs(graph, a, b-1)
    dfs(graph, a, b+1)
    return True


# 모든 인덱스 정보를 저장
index = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            index.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))


# 벽을 3개 세우는 모든 경우의 수
cases = list(combinations(index, 3))

for case in cases:
    copy_arr = copy.deepcopy(arr) # 원본 복사
    # 무작위 3곳의 빈공간에 벽을 세운다.
    for x, y in case:
        copy_arr[x][y] = 1
    # 바이러스가 있는 곳에서 bfs/dfs 수행
    for x, y in virus:
        dfs(copy_arr, x, y)

    # 연구소에 남아있는 안전영역 구하기.
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 0:
                safety += 1

    safety_list.append(safety)
    safety = 0 # 초기화

print(safety_list)
print(max(safety_list))








