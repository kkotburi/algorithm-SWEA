'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 온라인 강의
def dfs(v):
    print(v)
    visited[v] = 1

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    v, w = graph[i * 2], graph[i * 2 + 1]

    adj_list[v].append(w)
    adj_list[w].append(v)

visited = [0] * (V + 1)
dfs(1)