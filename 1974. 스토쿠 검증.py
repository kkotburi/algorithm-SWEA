import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        if not result:
            break

        check_row = [0] * 10
        check_col = [0] * 10

        for j in range(9):
            check_row[puzzle[i][j]] += 1
            check_col[puzzle[j][i]] += 1

        for k in range(1, 10):
            if check_row[k] > 1:
                result = 0
                break
            if check_col[k] > 1:
                result = 0
                break

    if result:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not result:
                    break

                check_triple = [0] * 10
                for row in range(3):
                    for col in range(3):
                        check_triple[puzzle[i + row][j + col]] += 1

                for verid in check_triple:
                    if verid == 2:
                        result = 0
                        break                

    print(f'#{test_case}', result)

#  GPT + 최묘석
# def valid(puzzle) :
#     nums = set(range(1, 10))

#     for row in puzzle:
#         if set(row) != nums:
#             return False
            
#     return True
 
# for test_case in range(1, T + 1):
#     puzzle = [list(map(int, input().split())) for _ in range(9)]

#     boxes = []
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             box = [
#                 puzzle[k][l]
#                 for k in range(i, i + 3)
#                 for l in range(j, j + 3)
#             ]
#             boxes.append(box)

#     result = int(
#         valid(puzzle)
#         and valid(zip(*puzzle))
#         and valid(boxes)
#     )

#     print(f'#{test_case}', result)