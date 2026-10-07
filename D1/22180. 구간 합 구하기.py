n, m = map(int, input().split())
nums = list(map(int, input().split()))
interval = []

for _ in range(m):
    interval.append(list(map(int, input().split())))

for i in range(m):
    sum = 0
    for j in range(interval[i][0] - 1, interval[i][1]):
        sum += nums[j]
    print(sum)