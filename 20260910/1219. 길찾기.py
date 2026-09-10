import sys
sys.stdin = open("input.txt", "r")

# for _ in range(10):
#     test_case, n = map(int, input().split())
#     city_list = list(map(int, input().split()))
#     adj_list = [[] for _ in range(100)]
#
#     for i in range(n):
#         v, w = city_list[i * 2], city_list[i * 2 + 1]
#         adj_list[v].append(w)
#
#     visited = [0] * 100
#
#     def dfs(v):
#         visited[v] = 1
#
#         for adj in adj_list[v]:
#             if not visited[adj]:
#                 dfs(adj)
#
#     dfs(0)
#
#     print(f'#{test_case}', visited[-1])

# 참고
for _ in range(10):
        test_case, n = map(int, input().split())
        citi_list = list(map(int, input().split()))
        adj_list = {i: [] for i in range(100)}

        for j in range(n):
            v, w = citi_list[j * 2], citi_list[j * 2 + 1]
            adj_list[v].append(w)

        visited = set()
        stack = [0]
        result = 0

        while stack:
            node = stack.pop()

            if node == 99:
                result = 1
                break

            # 방문하지 않은 노드 도착 시 stack 추가, visited 추가
            for m in range(len(adj_list[node])):
                if adj_list[node][m] not in visited:
                    visited.add(adj_list[node][m])
                    stack.append(adj_list[node][m])

        print(f'#{test_case}', result)