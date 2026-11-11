import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(row, total):
    global min_cost

    if total >= min_cost:
        return

    if row == N:
        min_cost = total
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            dfs(row + 1, total + V[row][i])
            used[i] = False

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')
    used = [False] * N

    dfs(0, 0)

    print(f'#{test_case} {min_cost}')


# 다른 사람 풀이 참고
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     V = [list(map(int, input().split())) for _ in range(N)]
#
#     size = 1 << N
#     dp = [float('inf')] * size
#     dp[0] = 0
#
#     for mask in range(size):
#         row = bin(mask).count('1')
#
#         for col in range(N):
#             bit = 1 << col
#
#             if mask & bit == 0:
#                 mask_next = mask | bit
#                 dp[mask_next] = min(dp[mask_next], dp[mask] + V[row][col])
#
#     print(f'#{test_case}', dp[-1])
