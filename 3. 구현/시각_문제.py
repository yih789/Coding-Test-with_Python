"""
정수 N,
00시 00분 00초 ~ N시 59분 59초까지 모든 시간 중 3이 하나라도 포함되는 경우의 수
"""

N = int(input())
count = 0

for i in range(N+1):
  for j in range(60):
    for k in range(60):
      #'000000'
      if '3' in str(i)+str(j)+str(k):
        count += 1

print(count)