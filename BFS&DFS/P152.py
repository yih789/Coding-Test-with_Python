from collections import deque

# N, M
N, M = map(int, input().split())

graph = []
# N행의 정보 입력
for _ in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

# 시작지점 (0, 0)
# 1이면 접근가능
# 1보다 크면 이미 접근
def bfs(graph, x, y):
    queue = deque()
    queue.append([0, 0])
    while queue:
        now_x, now_y = queue.popleft()
        # 상하좌우 중에서 방문하지 않은 곳 & 방문 가능한 곳(1) # 큐에 넣고, 방문처리
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 : # 벽인지 확인
                continue
            if graph[nx][ny] == 1: # 0이거나 1보다 크면 안된다.
                queue.append([nx, ny]) # 큐 삽입

                graph[nx][ny] += graph[now_x][now_y] # 방문처리
    return graph[N-1][M-1]

print(bfs(graph, 0, 0))










