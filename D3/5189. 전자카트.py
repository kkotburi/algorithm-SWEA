import sys
sys.stdin = open("input.txt", "r")

def permutation(x):
    global min_battery

    if x == N - 1:
        battery = 0

        for j in range(N - 1):
            battery += metrix[path[j]][path[j + 1]]
            
        battery += metrix[path[-1]][0]

        if battery < min_battery:
            min_battery = battery

        return

    for i in range(1, N):
        if used[i]:
            continue
        
        path.append(i)
        used[i] = True

        permutation(x + 1)

        path.pop()
        used[i] = False

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    metrix = [list(map(int, input().split())) for _ in range(N)]
    min_battery = 1000

    path = [0]
    used = [False] * N

    permutation(0)

    print(f'#{test_case}', min_battery)