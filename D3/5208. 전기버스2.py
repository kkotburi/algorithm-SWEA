import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    stop_list = list(map(int, input().split()))
    current = 1
    next = 0
    count = 0

    while next < stop_list[0]:
        for i in range(current + 1, current + 1 + stop_list[current]):
            if i + stop_list[i] >= next:
                next = i + stop_list[i]
                current = i
        count += 1

    print(f'#{test_case}', count)