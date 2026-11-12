import sys
sys.stdin = open("../input.txt", "r")

def explode(bricks, row, col):
    power = bricks[row][col]
    bricks[row][col] = 0

    for i in range(1, power):
        for dr, dc in directions:
            ndr, ndc = row + (dr * i), col + (dc * i)

            if 0 <= ndr < H and 0 <= ndc < W and bricks[ndr][ndc]:
                explode(bricks, ndr, ndc)


def solve(shot, bricks):
    global result

    bricks_left = sum(brick > 0 for row in bricks for brick in row)

    if bricks_left == 0:
        result = 0
        return

    if shot == N:
        result = min(result, bricks_left)
        return

    for col in range(W):
        for row in range(H):
            if bricks[row][col]:
                bricks_next = [[brick for brick in i] for i in bricks]

                explode(bricks_next, row, col)

                for j in range(W):
                    col_list = [bricks_next[k][j] for k in range(H) if bricks_next[k][j]]
                    col_next = [0] * (H - len(col_list)) + col_list

                    for nk in range(H):
                        bricks_next[nk][j] = col_next[nk]

                solve(shot + 1, bricks_next)

                break


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = float('inf')

    solve(0, bricks)

    print(f'#{tc} {result}')


# 다른 사람 풀이 참고
