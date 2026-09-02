n, m = map(int, input().split())
nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(m):
    row = []
    for j in range(1, n + 1):
        row.append(str(nums[-j][i]))
    print(" ".join(row))