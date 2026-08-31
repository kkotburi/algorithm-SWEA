import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    n = int(input())
    floors = list(map(int, input().split()))
    view = 0

    for i in range(2, n - 2):
        high = 0
        for floor in [floors[i - 2], floors[i - 1], floors[i + 1], floors[i + 2]]:
            if floor > high:
                high = floor
        if floors[i] > high:
            view += floors[i] - high

    print(f'#{test_case}', view)