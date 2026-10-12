name = "ABC"
n = len(name)

# def abc(level, path):
#     if level == 3:
#         print(path)
#         return

#     abc(level + 1, path)
#     abc(level + 1, path + [name[level]])

# abc(0, [])

for i in range(1 << n):
    arr = []

    for j in range(n):
        if i & (1 << j):
            arr.append(name[j])
        # if i & 0x1:
        #     arr.append(name[j])
        # i >>= 1

    print(arr)