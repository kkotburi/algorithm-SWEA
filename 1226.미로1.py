import sys
sys.stdin = open("input.txt", "r")

# 정답 코드 참고 및 GPT 활용
# for _ in range(10):
#     n = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     answer = 0

#     queue = []
#     visited = [[0] * 16 for _ in range(16)]

#     for i in range(16):
#         for j in range(16):
#             if maze[i][j] == 2:
#                 queue.append((i, j))
#                 visited[i][j] = 1

#     front = 0
#     direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     while front < len(queue):
#         i, j = queue[front]
#         front += 1

#         if maze[i][j] == 3:
#             answer = 1
#             break

#         for di, dj in direction:
#             ni, nj = i + di, j + dj

#             if maze[ni][nj] != 1 and visited[ni][nj] == 0:
#                 queue.append((ni, nj))
#                 visited[ni][nj] = 1

#     print(f'#{n}', answer)

for _ in range(10):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    answer = 0

    queue = []
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        i, j = queue.pop(0)

        if maze[i][j] == 3:
            answer = 1
            break

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj

            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1

    print(f'#{n}', answer)