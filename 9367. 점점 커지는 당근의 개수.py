import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    count_cur = 1
    count_max = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count_cur += 1

            if count_cur > count_max:
                count_max = count_cur

        else:
            count_cur = 1

    print(f'#{test_case}', count_max)