import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, 2):
    prize, count = map(str, input().split())
    max_prize = 0

    print(prize, count)

    # 조합으로 두 인덱스 선택 후 교환 재귀 함수


    print(f'#{test_case}', max_prize)