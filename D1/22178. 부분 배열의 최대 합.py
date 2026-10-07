#import sys
#sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
nums = list(map(int, input().split()))
max = 0

for i in range(len(nums) - m + 1):
    sum = 0
    for j in range(i, i + m):
        sum += nums[j]
    if sum > max:
        max = sum

print(max)