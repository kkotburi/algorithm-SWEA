import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def binary_search(n, r):
    l = 1
    c = int((l + r) / 2)
    result = 1

    while c != n:
        if c < n:
            l = c
        else:
            r = c
        result += 1
        c = int((l + r) / 2)

    return result

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    a = binary_search(A, P)
    b = binary_search(B, P)

    if a == b:
        answer = 0
    elif a < b:
        answer = "A"
    else:
        answer = "B"

    print(f'#{test_case} {answer}')


    # for test_case in range(1, T + 1):
    #     P, A, B = map(int, input().split())
    #     al, bl = 1, 1
    #     ar, br = P, P
    #     ac, bc = int((al + ar) / 2), int((al + ar) / 2)
    #     a, b = 1, 1

    #     while ac != A:
    #         if ac < A:
    #             al = ac
    #         else:
    #             ar = ac
    #         a += 1
    #         ac = (al + ar) // 2

    #     while bc != B:
    #         if bc < B:
    #             bl = bc
    #         else:
    #             br = bc
    #         b += 1
    #         bc = (bl + br) // 2

    #     if a == b:
    #         result = 0
    #     elif a < b:
    #         result = "A"
    #     else:
    #         result = "B"

    #     print(f'#{test_case} {result}')

