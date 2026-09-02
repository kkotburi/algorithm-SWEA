import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    gas = list(map(int, input().split()))
    now = 0
    count = 0

    for i in range(m):
        next = now + k

        if next >= n:
            break

        if next < gas[i]:
            count = 0
            break

        # if next == gas[i] or i + 1 >= m or gas[i + 1] > next:
        #     now = gas[i]
        # else:
        #     continue

        if i + 1 < m and gas[i + 1] <= next:
            continue
        else:
            now = gas[i]
        
        count += 1

    print(f'#{test_case}', count)