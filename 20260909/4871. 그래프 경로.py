import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for i in range(E):
        v, w = nodes[i][0], nodes[i][1]
        adj_list[v].append(w)
        adj_list[w].append(v)

    def dfs(start):
        visited[start] = 1

        for node in adj_list[start]:
            if not visited[node]:
                dfs(node)

    dfs(start)

    if visited[start] and visited[end]:
        result = 1
    else:
        result = 0

    print(f'#{test_case}', result)
