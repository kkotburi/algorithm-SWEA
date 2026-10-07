import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    _ = int(input())
    nums = list(map(int, input()))
    cards = [0] * 10
    max_count = 0
    max_num = 0

    for num in nums:
        cards[num] += 1

    for i in range(len(cards)):
        if cards[i] >= max_count:
            max_count = cards[i]
            max_num = i

    print(f'#{test_case}', max_num, max_count)