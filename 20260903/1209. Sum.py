import sys
sys.stdin = open("input.txt", "r")

for test_case in range(10):
    n = input()
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max = 0
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0

    for i in range(100):
        sum_row = 0
        sum_column = 0
        sum_diagonal_1 += matrix[i][i]
        sum_diagonal_2 += matrix[i][-1 - i]

        for j in range(100):
            sum_row += matrix[j][i]
            sum_column += matrix[i][j]

        if sum_row > max:
            max = sum_row
        if sum_column > max:
            max = sum_column

    if sum_diagonal_1 > max:
        max = sum_diagonal_1
    if sum_diagonal_2 > max:
        max = sum_diagonal_2

    print(f'#{n}', max)