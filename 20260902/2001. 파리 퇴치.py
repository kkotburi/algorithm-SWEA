import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        area = [list(map(int, input().split())) for _ in range(n)]
        max = 0

        for row in range(n - m + 1):
            for column in range(n - m + 1):
                sum = 0

                for i in range(m):
                    for j in range(m):
                        sum += area[row + i][column + j]
            
                if sum > max:
                    max = sum

        print(f'#{test_case}', max)