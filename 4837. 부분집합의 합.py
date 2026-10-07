import sys
sys.stdin = open("input.txt", "r")

nums = list(range(1, 13))

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0

    for i in range(2 ** 12):
        total = 0
        count = 0

        for j in range(12):
            if i & (1 << j):
                total += nums[j]
                count += 1

        if count == N and total == K:
            result += 1

    print(f'#{test_case}', result)


# GPT 활용 (비트 연산 사용 X)
# nums = list(range(1, 13))
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#
#     result = 0
#     groups = [[]]
#
#     for num in nums:
#         new_groups = []
#
#         for group in groups:
#             new_groups.append(group)
#             new_groups.append(group + [num])
#
#         groups = new_groups
#         print(groups)
#
#     for group in groups:
#         if len(group) == N and sum(group) == K:
#             result += 1
#
#     print(f'#{test_case}', result)
