import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def choose_sum(row, current_sum):
    global sum_min

    if current_sum >= sum_min:
        return
    
    if row == N:
        sum_min = min(sum_min, current_sum)
        return
    
    for col in range(N):
        if not check[col]:
            selected[row] = nums[row][col]
            check[col] = True

            choose_sum(row + 1, current_sum + nums[row][col])

            check[col] = False

for test_case in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    selected = [0] * N
    check = [False] * N
    sum_min = 10 * N

    choose_sum(0, 0)

    print(f'#{test_case}', sum_min)