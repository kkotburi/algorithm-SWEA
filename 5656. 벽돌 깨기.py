import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, 2):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    result = 0

    # 조합으로 구술 떨어뜨릴 곳 선택(횟수, 벽돌 0일 때 break)
    # 주변 벽돌 제거
    # 제거 벽돌 최댓값

    path = [None] * N
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def permutations(level, bricks):
        # global bricks

        if level == N:
            print("여기")
            for i in range(H):
                print(bricks[i])
            return


        for col in range(W):
            new_bricks = [[0] * W for _ in range(H)]
            for i in range(H):
                for j in range(W):
                    new_bricks[i][j] = bricks[i][j]
            for row in range(H):
                if new_bricks[row][col] != 0:
                    # 복사하고, 연쇄반응 일으키고 벽돌 정리하고

                    power = new_bricks[row][col]
                    new_bricks[row][col] = 0

                    # for i in range(1, bricks_next[row][col]):
                    #     for dr, dc in directions:
                    #         ndr, ndc = row + (dr * i), col + (dc * i)
                    #         if 0 <= ndr < H and 0 <= ndc < W:
                    #             bricks[ndr][ndc] = 0

                    permutations(level + 1, new_bricks)
                    bricks[row][col] = power

                    break

    permutations(0)

    print(f'#{test_case} {result}')


# 다른 사람 풀이 참고
# def solve(N, W, H, board):
#     answer = W * H
#     directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
#
#     def explode(board, row, col):
#         power = board[row][col]
#         board[row][col] = 0
#
#         for dr, dc in directions:
#             for distance in range(1, power):
#                 nr = row + dr * distance
#                 nc = col + dc * distance
#
#                 if not (0 <= nr < H and 0 <= nc < W):
#                     break
#
#                 if board[nr][nc]:
#                     explode(board, nr, nc)
#
#     def apply_gravity(board):
#         for col in range(W):
#             bricks = [
#                 board[row][col]
#                 for row in range(H)
#                 if board[row][col]
#             ]
#             column = [0] * (H - len(bricks)) + bricks
#
#             for row, value in enumerate(column):
#                 board[row][col] = value
#
#     def search(N_left, board):
#         nonlocal answer
#
#         remaining = sum(value > 0 for row in board for value in row)
#
#         if remaining == 0 or N_left == 0:
#             answer = min(answer, remaining)
#             return
#
#         for col in range(W):
#             row = next(
#                 (row for row in range(H) if board[row][col]),
#                 None,
#             )
#             if row is None:
#                 continue
#
#             next_board = [row[:] for row in board]
#             explode(next_board, row, col)
#             apply_gravity(next_board)
#             search(N_left - 1, next_board)
#
#             if answer == 0:
#                 return
#
#     search(N, board)
#
#     return answer
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(H)]
#
#     print(f"#{test_case} {solve(N, W, H, board)}")


# 연습
# T = int(input())
#
# def solution(N, W, H, board):
#     answer = W * H
#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#     def search(N, board):
#         global answer
#
#         remaining = sum(value > 0 for row in board for value in row)
#
#         if remaining == 0 or N == 0:
#             answer = min(answer, remaining)
#             return
#
#         for i in range(W):
#             row = 0
#
#             for j in range(H):
#                 if board[j][i]:
#                     row = j
#                     break
#
#             if not row:
#                 continue
#
#
#
#     return answer
#
#
# for test_case in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(H)]
#
#     result = solution(N, W, H, board)
#
#     print(f'#{test_case} {result}')