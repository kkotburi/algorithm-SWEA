import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case, n = map(int, input().split())
    city_list = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]

    for i in range(n):
        v, w = city_list[i * 2], city_list[i * 2 + 1]
        adj_list[v].append(w)

    visited = [0] * 100

    def dfs(v):
        visited[v] = 1

        for adj in adj_list[v]:
            if not visited[adj]:
                dfs(adj)

    dfs(0)

    print(f'#{test_case}', visited[-1])

# 참고
# for _ in range(10):
#         test_case, n = map(int, input().split())
#         city_list = list(map(int, input().split()))
#         adj_list = [[] for _ in range(100)]
#
#         for j in range(0, len(city_list), 2):
#             v, w = city_list[j], city_list[j + 1]
#             adj_list[v].append(w)
#
#         visited = {0}
#         stack = [0]
#         result = 0
#
#         while stack:
#             city = stack.pop()
#
#             if city == 99:
#                 result = 1
#                 break
#
#             for next in adj_list[city]:
#                 if next not in visited:
#                     visited.add(next)
#                     stack.append(next)
#
#         print(f'#{test_case}', result)