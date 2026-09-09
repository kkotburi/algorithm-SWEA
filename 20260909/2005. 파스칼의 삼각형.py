T = int(input())

# for test_case in range(1, T + 1):
#     n = int(input())
#     fibonacci = [[1]]
#
#     for i in range(1, n):
#         nums = [1]
#
#         for j in range(1, i):
#             nums.append(fibonacci[i - 1][j - 1] + fibonacci[i - 1][j])
#
#         nums.append(1)
#         fibonacci.append(nums)
#
#     print(f'#{test_case}')
#     for row in range(n):
#         print(" ".join(map(str, fibonacci[row])))

for test_case in range(1, T + 1):
    n = int(input())
    triangle = []

    print(f'#{test_case}')

    for i in range(n):
        nums = [1]

        for j in range(1, i + 1):
            if j != i:
                nums.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            else:
                nums.append(1)

        triangle.append(nums)
        print(*nums)
