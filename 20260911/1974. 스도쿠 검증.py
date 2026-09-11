import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 행

    # 열

    # 3 * 3 영역

    print(f'#{test_case}', answer)