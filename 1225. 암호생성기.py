import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case = int(input())
    nums = list(input().split())

    print(f'#{test_case}', nums)