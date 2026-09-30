import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    capaity = sorted(list(map(int, input().split())), reverse=True)

    weight_index = 0
    total = 0

    for i in range(M):
        for j in range(weight_index, N):
            if weight[j] <= capaity[i]:
                weight_index = j + 1
                total += weight[j]
                break

    print(f'#{test_case}', total)

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     weight = sorted(list(map(int, input().split())))
#     capaity = sorted(list(map(int, input().split())))

#     weight_index = N
#     total = 0

#     for i in range(M - 1, -1, -1):
#         for j in range(weight_index - 1, -1, -1):
#             if weight[j] <= capaity[i]:
#                 weight_index = j
#                 total += weight[j]
#                 break

#     print(f'#{test_case}', total)