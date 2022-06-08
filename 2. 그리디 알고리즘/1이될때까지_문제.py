"""
어떤 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능하다.
  1. N에서 1을 뺀다.
  2. N을 K로 나눈다.
"""

# 빼기 보다 나누기가 빠르게 감소하므로 최대한 많은 나누기를 수행해야 한다.
# N을 나눌 수 있는 상태로 만들고, 나누기 수행

N, K = map(int, input().split())
count = 0

while True:
    target = (N // K) * K
    count += (N - target)
    N = target

    if (N < K):
        break

    N //= K
    count += 1

# N < K 일때, N만큼 count가 증가했기 때문에 빼기를 한 번 취소하면
# N = 1이 된다.
count -= 1
print(count)

# 그리디 방법이 정당한가?
# 빼기보다 나누기를 통해서 기하급수적으로 빠르게 줄일 수 있다.