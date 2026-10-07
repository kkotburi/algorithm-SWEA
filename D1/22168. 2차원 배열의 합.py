# T = list(map(int, input().split()))
# num_sum = 0

# for test_case in range(1, T[0] + 1):
#     row_list = list(map(int, input().split()))
#     for num in row_list:
#         num_sum += num

# print(num_sum)

row, col = map(int, input().split())
num_sum = 0

for _ in range(row):
    row_list = list(map(int, input().split()))

    for num in row_list:
        num_sum += num

print(num_sum)