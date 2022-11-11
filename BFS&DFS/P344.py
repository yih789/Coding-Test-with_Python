import heapq

# 행렬 크기, 바이러스 범위
N, K = map(int, input().split())

# S초 후에 (X, Y)위치
S, X, Y = map(int, input().split())

# 연구소 N X N, 시작 위치 (1, 1)
# 마지막 결과 출력 시 인덱스 조정 +1 필요
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 바이러스 정보 저장
viruses = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0: # 바이러스 라면
            viruses.append((i, j, arr[i][j])) # (x, y)에 크기가 k인 바이러스

# 상, 하, 좌, 우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(graph, virus, s):
    heap = []
    for x, y, k in virus:
        heapq.heappush(heap, (0, k, x, y))
    print(heap)

    while heap:
        time, k, x, y = heapq.heappop(heap)
        print(time, k, x, y)
        # 상하좌우 중 방문 가능한 곳을 모두 큐에 삽입
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                print(nx, ny)
                continue
            if graph[nx][ny] == 0:
                # 방문처리
                graph[ny][ny] = k
                # 힙 삽입
                print(time+1, s)
                if (time+1) <= s:
                    heapq.heappush(heap, (time+1, k, nx, ny))
            continue
        print(graph)

bfs(arr, viruses, S)
print(arr[X-1][Y-1])
