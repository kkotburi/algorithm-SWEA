n = 6
arr = [i for i in range(n)]
rank = [0] * n

def find(member):
    if arr[member] == member:
        return member

    ret = find(arr[member])
    arr[member] = ret

    return ret

def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa == fb:
        return

    # arr[fb] = fa
    if rank[fa] == rank[fb]:
        arr[fb] = fa
        rank[fa] += 1
    elif rank[fa] > rank[fb]:
        arr[fa] = fb
    else:
        arr[fb] = fa

union(0, 1)
union(3, 4)
union(1, 4)
union(1, 3)
union(5, 4)

x, y = map(int, input().split())
if find(x) == find(y):
    print("They are union")
else:
    print("They aren't nuion")