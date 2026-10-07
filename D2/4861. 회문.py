import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    letters_list = [input() for _ in range(n)]

    # 가로
    for letters in letters_list:
        for i in range(n - m + 1):
            for j in range(m // 2):
                if letters[i + j] == letters[i + m - 1 - j]:
                    if j == m // 2 - 1:
                        palindrome = letters[i:i+m]
                else:
                    break

    # 세로
    for row in range(n):
        for column in range(n):
            for i in range(m // 2):
                if letters_list[]


    print(f'#{test_case}', palindrome)