import sys
sys.stdin = open("input.txt", "r")

# def create_password(nums):
#     while True:
#         for decrease_amount in range(1, 6):
#             num = nums[0] - decrease_amount
#             nums = nums[1:]
#             nums.append(max(num, 0))

#             if num <= 0:
#                 return nums

# for _ in range(10):
#     test_case = int(input())
#     nums = list(map(int, input().split()))

#     result = create_password(nums)

#     print(f'#{test_case}', *result)

# 정답 코드 참고 및 GPT 활용
def create_password(nums):
    decrement = 1

    while True:
        num = nums.pop(0) - decrement
 
        if num <= 0:
            nums.append(0)
            return nums

        nums.append(num)

        decrement += 1
        if decrement > 5:
            decrement = 1

for _ in range(10):
    test_case = int(input())
    nums = list(map(int, input().split()))
 
    result = create_password(nums)
 
    print(f'#{test_case}', *result)

# deque 활용
# from collections import deque
#
# def create_password(nums):
#     nums = deque(nums)
#     decrease = 1
#
#     while True:
#         num = nums.popleft() - decrease
#
#         if num <= 0:
#             nums.append(0)
#             return nums
#
#         nums.append(num)
#         decrease += 1
#
#         if decrease > 5:
#             decrease = 1
#
# for _ in range(10):
#     test_case = int(input())
#     nums = list(map(int, input().split()))
#
#     result = create_password(nums)
#
#     print(f'#{test_case}', *result)k