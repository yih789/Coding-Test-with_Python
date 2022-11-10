# N명의 모험가
N = int(input())

# N명의 모험가의 공포도
arr = list(map(int, input().split()))

# 오름차순 정렬
arr.sort()

# 공포도가 낮은 순서대로 자신의 공포도에 맞는 인원 그룹에 포함시키면서 카운팅
count = 0 # 그룹 수
need = 0 # 현재 모아야 하는 인원
collection = 0 # 모집 중인 그룹 내 인원


for x in arr:
    need = x
    collection += 1
    if collection == need:
        count += 1
        collection = 0


print(count)