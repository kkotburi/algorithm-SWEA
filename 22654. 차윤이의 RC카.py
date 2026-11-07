import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    Q = int(input())
    commands = [list(input().split()) for _ in range(Q)]

    print(commands)
    print(f'#{tc}')