import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    letters = input()
    remain = []

    for letter in letters:
        if len(remain) and letter == remain[-1]:
            remain.pop()
        else:
            remain.append(letter)

    print(f'#{test_case}', len(remain))