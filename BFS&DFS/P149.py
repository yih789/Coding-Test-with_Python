# N X M
N, M = map(int, input().split())

# array
graph = []

# N행의 정보 입력
for _ in range(N):
    graph.append(list(map(int, input())))

# DFS # 재귀적 가능
def dfs(graph, x, y):
    if x < 0 or x > N-1 or y < 0 or y > M-1 or graph[x][y] == 1:
        return False

    # 시작지점 방문처리
    graph[x][y] = 1

    # 인접지점 상하좌우 모두 확인
    dfs(graph, x, y-1) #상
    dfs(graph, x, y+1) #하
    dfs(graph, x-1, y) #좌
    dfs(graph, x+1, y) #우
    return True

# 결과값
result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            if dfs(graph, i, j) == True:
                result += 1

print(result)



