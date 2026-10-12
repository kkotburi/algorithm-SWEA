# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


# SW 문제 해결 기본
# def dfs(v):
#     print(v)
#     visited[v] = 1

#     for w in adj_list[v]:
#         if visited[w] == 0:
#             dfs(w)

# V, E = map(int, input().split())
# graph = list(map(int, input().split()))
# adj_list = [[] for _ in range(V + 1)]

# for i in range(E):
#     v, w = graph[i * 2], graph[i * 2 + 1]

#     adj_list[v].append(w)
#     adj_list[w].append(v)

# print(adj_list)
# visited = [0] * (V + 1)
# dfs(1)


# SW 문제 해결 응용
name = "BACD"

# 인접 행렬 => 가능한 모든 정점 1회씩 탐색
# metrix = [
#     [0, 0, 1, 1],
#     [1, 0, 1, 0],
#     [1, 0, 0, 1],
#     [0, 0, 0, 0]
# ]
# used = [0] * 4

# def dfs(now):
#     print(name[now], end = ' ')

#     for i in range(4):
#         if metrix[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             dfs(i)

# 인접 리스트 => 가능한 모든 정점 1회씩 탐색, 도착 경우의 수
# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3
n, m = map(int, input().split())
metrix = [[] for _ in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    metrix[start].append(end)

used = [0] * n
count = 0

def dfs(now):
    print(name[now], end = ' ')
    global count
    if now == 3:
        count += 1

    for i in metrix[now]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)
            used[i] = 0

# 탐색 시작 index에 1 중복 확인
used[1] = 1
# 탐색 시작 index
dfs(1)
print(count)