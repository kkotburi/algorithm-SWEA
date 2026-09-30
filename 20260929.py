# def dfs(index):
#     nums = [1 for _ in range(4)]
#
#     if index:
#     index += 1
#
#     for i in range(len(nums)):
#         print(nums[i] + 1)
#
# dfs(0)


# # 누적합 구하기 - 재귀 DFS 구현 시 global VS 매개 변수
# arr = [1,3, 5, 7]
#
# def abc(level, arr_sum):
#     if level == 3:
#         print(arr_sum, end = ' ')
#         return
#
#     abc(level + 1, arr_sum + arr[level + 1])
#     abc(level + 1)
#
# abc(0, arr[0])


# # level = 3
# # branch = 4
# card = "ABCD"
#
# # 경로 저장하는 배열의 크기 => level
# path = [""] * 3
#
# def abc(level):
#     if level == 3:
#         for i in range(level):
#             print(path[i], end = ' ')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = card[i]
#         abc(level + 1)

n = int(input())
path = [0] * n

def abc(level):
    if level == n:
        print(*path)
        return

    for i in range(1, 4):
        # 들어갈 예정인 곳을 path 배열에 저장
        path[level] = i
        abc(level + 1)

abc(0)