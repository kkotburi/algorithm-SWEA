import sys
sys.stdin = open("input.txt", "r")

def find_land(x, y, metrix):
    metrix[x][y] = "W"

    for v, h in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x_next = x + v
        y_next = y + h

        if 0 <= x_next < N and 0 <= y_next < M and metrix[x_next][y_next] == "L":
            find_land(x_next, y_next, metrix)

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sealand = [list(input()) for _ in range(N)]
    land = 0

    for i in range(N):
        for j in range(M):
            if sealand[i][j] == "L":
                land += 1
                find_land(i, j, sealand)

    print(f'#{test_case}', land)