import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]

    for i in range(E):
        v, w = map(int, input().split())
        adj_list[v].append(w)

    start, end = map(int, input().split())
    visited = [0] * (V + 1)

    def dfs(start):
        visited[start] = 1

        for adj in adj_list[start]:
            if not visited[adj]:
                dfs(adj)

    dfs(start)

    print(f'#{test_case}', visited[end])