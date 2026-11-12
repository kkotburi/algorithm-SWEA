import sys
sys.stdin = open("input.txt", "r")

direction = [(-1, 0 )]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    energies = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    print(energies)

    print(f'{tc} {result}')
