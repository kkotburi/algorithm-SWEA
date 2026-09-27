import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = [0] * 12
    count = 0

    print(f'#{test_case}', count)