import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    area = [[0] * 10 for _ in range(10)]
    n = int(input())
    purple = 0

    for _ in range(n):
        i_start, j_start, i_end, j_end, color = list(map(int, input().split()))
        for i in range(i_start, i_end + 1):
            for j in range(j_start, j_end + 1):
                area[i][j] += color

    for row in range(10):
        for column in range(10):
            if area[row][column] == 3:
                purple += 1
    
    print(f'#{test_case}', purple)