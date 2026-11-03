import sys
sys.stdin = open("../input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    arr = []

    for i in range(0, 5):
        arr.append(nums[i])
        arr.append(nums[N - 1 - i])
        # arr.extend([nums[i], nums[N - 1 - i]])

    print(f'#{test_case}', *arr)
