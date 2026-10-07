import sys
sys.stdin = open("input.txt", "r")

# for test_case in range(1, 11):
#     dump = int(input())
#     boxes = list(map(int, input().split()))
#
#     while dump:
#         max_num = 1
#         max_idx = 0
#         min_num = 1000
#         min_idx = 0
#
#         for i in range(len(boxes)):
#             if boxes[i] > max_num:
#                 max_num = boxes[i]
#                 max_idx = i
#             if boxes[i] < min_num:
#                 min_num = boxes[i]
#                 min_idx = i
#
#         boxes[max_idx] -= 1
#         boxes[min_idx] += 1
#         dump -= 1
#
#     result_max = 1
#     result_min = 1000
#     for num in boxes:
#         if num > result_max:
#             result_max = num
#         if num < result_min:
#             result_min = num
#
#     print(f'#{test_case}', result_max - result_min)

for test_case in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))

    for _ in range(N):
        nums[nums.index(max(nums))] -= 1
        nums[nums.index(min(nums))] += 1

    print('#%d' % test_case, max(nums) - min(nums))

# GPT
def dump_boxes(nums, count):
    for _ in range(count):
        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))

        nums[max_idx] -= 1
        nums[min_idx] += 1

    return max(nums) - min(nums)

for test_case in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    
    result = dump_boxes(nums, N)

    print(f'#{test_case}', result)

# 참고 코드
# for test_case in range(1, 11):
#     dump = int(input())
#     boxes = list(map(int, input().split()))
#
#     for _ in range(dump):
#         boxes.sort()
#         boxes[0] += 1
#         boxes[-1] -= 1
#
#     boxes.sort()
#
#     print(f"#{test_case}", boxes[-1] - boxes[0])

# for test_case in range(1, 11):
#     dump = int(input())
#     boxes = list(map(int, input().split()))

#     count = [0] * 101
#     for i in range(100):
#         count[boxes[i]] += 1
 
#     max_idx = 100
#     min_idx = 0
#     for _ in range(dump):
#         for max in range(max_idx, 0, -1):
#             if count[max]:
#                 max_idx = max
#                 break
#         for min in range(min_idx, 100):
#             if count[min]:
#                 min_idx = min
#                 break
 
#         count[max_idx] -= 1
#         count[max_idx - 1] += 1
#         count[min_idx] -= 1
#         count[min_idx + 1] += 1
 
#     if not count[max_idx]:
#         max_idx -= 1
#     if not count[min_idx]:
#         min_idx += 1
 
#     print(f'#{test_case}', max_idx - min_idx)