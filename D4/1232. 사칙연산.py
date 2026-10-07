import sys
sys.stdin = open("input.txt", "r")

# for test_case in range(1, 11):
#     n = int(input())
#     nodes = [list(input().split(" ")) for _ in range(n)]
#     answer = 0
#
#     print(f'#{test_case}', nodes)

# 정답 코드 참고 및 GPT 활용
ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

for test_case in range(1, 11):
    N = int(input())
    tree = [None] * (N + 1)

    for _ in range(N):
        node = input().split()
        idx = int(node[0])

        if node[1].isdigit():
            tree[idx] = int(node[1])
        else:
            tree[idx] = (node[1], int(node[2]), int(node[3]))

    for i in range(N, 0, -1):
        if isinstance(tree[i], tuple):
            op, l, r = tree[i]
            tree[i] = ops[op](tree[l], tree[r])

    print(f'#{test_case}', tree[1])