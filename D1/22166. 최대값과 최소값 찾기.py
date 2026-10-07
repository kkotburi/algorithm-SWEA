n = int(input())
num_list = list(map(int, input().split()))
num_max = num_list[0]
num_min = num_list[0]

for num in num_list:
    if num > num_max:
        num_max = num
    if num < num_min:
        num_min = num

print(num_max, num_min)