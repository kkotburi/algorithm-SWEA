import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = list(range(1, (N ** 2) + 1))
    # print(N, nums)
    result = []
    [(0, 1), (1, 0), (0, -1), (-1, 0)]

    print(f'{test_case}')
    for row in result:
        print(*result)
