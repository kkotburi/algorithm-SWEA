import sys
sys.stdin = open("input.txt", "r")

# for test_case in range(1, 11):
#     N = int(input())
#     nums = list(map(int, input().split()))

#     while N:
#         nums[nums.index(max(nums))] -= 1
#         nums[nums.index(min(nums))] += 1
#         N -= 1

#     print('#%d' % test_case, max(nums) - min(nums))

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

# 참고 코드
for test_case in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    cnt_list = [0] * 101
    for i in range(100):
        cnt_list[box_list[i]] += 1
 
    max_idx = 100
    min_idx = 0
    for j in range(dump):
        # 가장 높은 상자 인덱스
        for m in range(max_idx, 0, -1):
            if cnt_list[m] != 0:
                max_idx = m
                break
        # 가장 낮은 상자 인덱스
        for n in range(min_idx, 100):
            if cnt_list[n] != 0:
                min_idx = n
                break
 
        # dump 수행
        cnt_list[max_idx] -= 1
        cnt_list[max_idx-1] += 1
        cnt_list[min_idx] -= 1
        cnt_list[min_idx+1] += 1
 
    # 덤프 수행 완료 후 최종 계산
    if cnt_list[max_idx] == 0:
        max_idx -= 1
    if cnt_list[min_idx] == 0:
        min_idx += 1
 
    print(f'#{test_case} {max_idx - min_idx}')

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