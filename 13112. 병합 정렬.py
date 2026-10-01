arr = [2, 3, 5, 7, 1, 2, 5, 9]
start = 0
end = 7
mid = (start + end) // 2

a = start
b = mid + 1
result = []

while 1:
    print(result)

    if a > mid and b > end:
        break

    if a > mid:
        result.append(arr[b])
        b += 1
    elif b > end:
        result.append(arr[a])
        a += 1
    elif arr[a] <= arr[b]:
        result.append(arr[a])
        a += 1
    else:
        result.append(arr[b])
        b += 1

print(*result)