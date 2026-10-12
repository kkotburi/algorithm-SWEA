import heapq

# 우선순위 큐
arr = []
heapq.heappush(arr, 3)
heapq.heappush(arr, 234)
heapq.heappush(arr, 23)
heapq.heappush(arr, 12)
heapq.heappush(arr, 31)

# while arr:
#     node = heapq.heappop(arr)
#     print(node, end = ' ')

# heap = []
# for i in range(len(arr)):
#     heapq.heappush(heap, -arr[i])

heap = list(map(lambda x: -x, arr))
heapq.heapify(heap)

for i in range(len(heap)):
    print(-heapq.heappop(heap), end = ' ')


# prim 구현
n, m = map(int, input().split())
arr = [[] for _ in range(n)]

# 무방향 graph이므로 양방향 저장
for _ in range(m):
    start, end, cost = map(int, input().split())

    arr[start].append((cost, end))
    arr[end].append((cost, start))  

used = [0] * n
heap = []

heapq.heappush(heap, (0, 0))

total = 0
count = 0

while heap:
    cost, now = heapq.heappop(heap)

    if used[now] == 1:
        continue

    used[now] = 1
    total += cost
    count += 1

    if count == n:
        break

    for next_cost, next_node in arr[now]:
        if used[next_node] == 0:
            heapq.heappush(heap, (next_cost, next_node))

print(total)