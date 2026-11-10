import sys
sys.stdin = open("../sample_in.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    M = int(input())
    N = 0
    S = 0

    while S < M:
        N += 1
        S += N

    print(f'#{test_case} {N}')
