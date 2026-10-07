import sys
sys.stdin = open("input.txt", "r")

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "//": lambda a, b: a // b,
    "%": lambda a, b: a % b,
    "**": lambda a, b: a ** b
}

T = int(input())

for test_case in range(1, 1 + T):
    code = input().split()
    stack = []
    error = False

    for token in code:
        if token == ".":
            break

        try:
            stack.append(int(token))
        except ValueError:
            if len(stack) < 2:
                error = True
                break

            b, a= stack.pop(), stack.pop()
            stack.append(operations[token](a, b))

    if not error and len(stack) == 1:
        result = int(stack[0])
    else:
        result = "error"

    print(f'#{test_case}', result)