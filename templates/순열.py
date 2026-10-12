# 중복 순열
# n, m = 3, 4

# card = "ABCD"
# path = [None] * n

# def abc(level):
#     if level == 3:
#         print(path)
#         return

#     for i in range(m):
#         path[level] = card[i]
#         abc(level + 1)
#         path[level] = None

# abc(0)

n, m = map(int, input().split())
path = [None] * n
used = [False] * m

def abc(level):
    if level == n:
        print(path)
        return

    for i in range(m):
        if used[i]:
            continue
        path[level] = i
        used[i] = True
        abc(level + 1)
        path[level] = None
        used[i] = False

abc(0)