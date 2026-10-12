n, m = 3, 4

card = "ABCD"
path = [None] * n

def abc(level, start):
    if level == n:
        print(path)
        return

    for i in range(start, m):
        path[level] = card[i]
        abc(level + 1, i + 1)
        # 중복 조합
        # abc(level + 1, i)
        path[level] = None

abc(0, 0)