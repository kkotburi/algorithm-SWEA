import sys
sys.stdin = open("input.txt", "r")

for test_case in range(10):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    now = 0

    for end in range(100):
        if ladder[99][end] == 2:
            now = end
            break

    for i in range(98, 0, -1):
        if now > 0 and ladder[i][now - 1]:
            while now > 0 and ladder[i][now - 1]:
                now -= 1
        else:
            while now < 98 and ladder[i][now + 1]:
                now += 1

    print(f'#{n}', now)

for test_case in range(10):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    now = 0
    # 시작 위치 선정
    for end in range(100):
        if ladder[99][end] == 2:
            now = end
    # 위로 이동
    for i in range(99, -1, -1):
        # 좌로 위치 전환
        if now - 1 >= 0 and ladder[i][now - 1]:
            while now - 1 >= 0 and ladder[i][now - 1]:
                now -= 1
        # 우로 위치 전환
        else:
            while now + 1 <= 99 and ladder[i][now + 1]:
                now += 1

    print(f'#{n}', now)