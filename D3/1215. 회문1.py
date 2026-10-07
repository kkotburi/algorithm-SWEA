import sys
sys.stdin= open("input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    matrix = [input() for _ in range(8)]
    count = 0

    for row in range(8):
        for i in range(9 - n):
            row_palindrome = 0
            col_palindrome = 0

            for j in range(n // 2):
                if matrix[row][i + j] == matrix[row][i + n - 1 - j]:
                    row_palindrome += 1
                if matrix[i + j][row] == matrix[i + n - 1 - j][row]:
                    col_palindrome += 1

            if row_palindrome == n // 2:
                count += 1
            if col_palindrome == n // 2:
                count += 1

    print(f'#{test_case}', count)