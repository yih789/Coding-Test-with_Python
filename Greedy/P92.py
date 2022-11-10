# 배열 크기, 연산 횟수, 반복 가능 횟수
N, M, K = map(int, input().split())

# 배열 정보
arr = list(map(int, input().split()))

# 배열 내림차순 정렬
arr.sort(reverse=True)

result = 0

# 첫 번째 원소 최대합
result += (K * (M // K)) * arr[0]
result += (M % K) * arr[1]

print(result)