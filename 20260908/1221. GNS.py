import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(1, T + 1):
    test_case, n = map(str, input().split())
    nums = list(map(str, input().split()))
    result = []

    num_dict = {
        "ZRO" : [0, 0],
        "ONE" : [1, 0],
        "TWO" : [2, 0],
        "THR" : [3, 0],
        "FOR" : [4, 0],
        "FIV" : [5, 0],
        "SIX" : [6, 0],
        "SVN" : [7, 0],
        "EGT" : [8, 0],
        "NIN" : [9, 0]
        }

    for num in nums:
        num_dict[num][1] += 1

    for i in range(10):
        for key, value in num_dict.items():
            if value[0] == i:
                for _ in range(value[1]):
                    result.append(key)

    print(f'{test_case}\n{" ".join(result)}')

# for _ in range(1, T + 1):
#     test_case, n = map(str, input().split())
#     nums = list(map(str, input().split()))
#     result = []

#     num_dict = {
#         "ZRO" : 0,
#         "ONE" : 0,
#         "TWO" : 0,
#         "THR" : 0,
#         "FOR" : 0,
#         "FIV" : 0,
#         "SIX" : 0,
#         "SVN" : 0,
#         "EGT" : 0,
#         "NIN" : 0
#         }

#     for num in nums:
#         num_dict[num] += 1

#     for key, value in num_dict.items():
#         for _ in range(value):
#             result.append(key)

#     print(f'{test_case}\n{" ".join(result)}')