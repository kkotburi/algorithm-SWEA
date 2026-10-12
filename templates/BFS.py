# 너비 우선 탐색
# 4 6
# 0 1
# 0 2
# 1 2
# 1 3
# 2 1
# 2 3
from collections import deque

name = "ABCD"
n, m = map(int, input().split())
metrix = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    metrix[a].append(b)

print(metrix)

used = [0] * n
# q = deque()
q = []

used[0] = 1
q.append(0)

while q:
    # now = q.popleft()
    now = q[0]
    q = q[1:len(q)]
    print(name[now], end = ' ')

    for i in metrix[now]:
        if used[i] == 0:
            used[i] = 1
            q.append(i)