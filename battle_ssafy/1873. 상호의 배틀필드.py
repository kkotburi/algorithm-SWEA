import sys
sys.stdin = open("input.txt", "r")

# 다른 사람 풀이 참고 및 GPT 활용
# CONTROL = {
#     "U": (-1, 0, "^"),
#     "D": (1, 0, "v"),
#     "L": (0, -1, "<"),
#     "R": (0, 1, ">"),
# }
# SHOOT = {v[2]: v[:2] for v in CONTROL.values()}

# T = int(input())

# for test_case in range(1, T + 1):
#     H, W = map(int, input().split())
#     field = [list(input()) for _ in range(H)]
#     N = input()
#     commands = input()

#     for i in range(H):
#         for j in range(W):
#             if field[i][j] in SHOOT:
#                 x, y = i, j
#                 break

#     for command in commands:
#         if command in CONTROL:
#             dx, dy, d = CONTROL[command]
#             field[x][y] = d
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == ".":
#                 field[x][y] = "."
#                 field[nx][ny] = d
#                 x, y = nx, ny
#         else:
#             dx, dy = SHOOT[field[x][y]]
#             sx, sy = x + dx, y + dy
#             while 0 <= sx < H and 0 <= sy < W:
#                 if field[sx][sy] == "*":
#                     field[sx][sy] = "."
#                     break
#                 elif field[sx][sy] == "#":
#                     break
#                 sx += dx
#                 sy += dy

#     print(f'#{test_case}', end=' ')
#     for row in field:
#         print(''.join(row))

# 다른 사람 풀이
DIRECTION = '^v<>'
CONTROL = 'UDLR'
MOVE = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = input()
    commands = input()

    for i in range(H):
        for j in range(W):
            if field[i][j] in DIRECTION:
                y, x = i, j
                d = DIRECTION.index(field[i][j])

    for command in commands:
        if command == 'S':
            dy, dx = MOVE[d]
            sy, sx = y + dy, x + dx
            while 0 <= sy < H and 0 <= sx < W:
                if field[sy][sx] == '#':
                    break
                if field[sy][sx] == '*':
                    field[sy][sx] = '.'
                    break
                sy += dy
                sx += dx
        else:
            d = CONTROL.index(command)
            dy, dx = MOVE[d]
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and field[ny][nx] == '.':
                field[y][x] = '.'
                field[ny][nx] = DIRECTION[d]
                y, x = ny, nx
            else:
                field[y][x] = DIRECTION[d]

    print(f'#{tc}', end=' ')
    for row in field:
        print(''.join(row))