# n = int(input())
# nums = sorted(list(map(int, input().split())))
# count = 1

# for i in range(0, len(nums)):
#     if i + 1 < len(nums) and nums[i] == nums[i + 1]:
#         count += 1
#     else:
#         print(nums[i], count)
#         count = 1

n = int(input())
nums = list(map(int, input().split()))
counts = {}

for num in nums:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

for num in sorted(counts):
    print(num, counts[num])