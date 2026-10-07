import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    num_max = nums[0]
    num_min = nums[0]
    
    for i in range(1, n):
        if nums[i] > num_max:
            num_max = nums[i]
        elif nums[i] < num_min:
            num_min = nums[i]

    print(f'#{test_case}', num_max - num_min)