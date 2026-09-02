import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    sum_max = 2
    sum_min = 1000000

    for i in range(n - m + 1):
        sum_num = 0
        for j in range(i, i + m):
            sum_num += nums[j]
        if sum_num > sum_max:
            sum_max = sum_num
        if sum_num < sum_min:
            sum_min = sum_num

    print(f'#{test_case}', sum_max - sum_min)