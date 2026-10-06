import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    global result

    if v == G:
        result += 1
        return

    visited[v] = 1

    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)
        visited[w] = 0

T = int(input())

for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    graph = list(map(int, input().split()))
    S, G = map(int, input().split())

    adj_list = [[] for _ in range(N + 1)]
    result = 0

    for i in range(E):
        v, w = graph[i * 2], graph[i * 2 + 1]
        adj_list[v].append(w)

    visited = [0] * (N + 1)
    dfs(S)

    print(f'#{test_case}', result)