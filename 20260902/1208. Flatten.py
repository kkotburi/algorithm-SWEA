import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    while dump > 0:
        max = 1
        max_idx = 0
        min = 1000
        min_idx = 0

        for i in range(len(boxes)):
            if boxes[i] > max:
                max = boxes[i]
                max_idx = i
            if boxes[i] < min:
                min = boxes[i]
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        if dump == 1:
            print(f'#{test_case}', max - min)

        dump -= 1