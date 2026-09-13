import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    letters = input()
    sum = 0

    for token in range(0, n, 2):
        sum += int(letters[token])

    print(f'#{test_case}', sum)