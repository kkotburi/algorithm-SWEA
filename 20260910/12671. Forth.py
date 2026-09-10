import sys
sys.stdin = open("input.txt", "r")

def operator(a, b, letter):
    operations = {
        "+": lambda: a + b,
        "-": lambda: a - b,
        "*": lambda: a * b,
        "/": lambda: a / b,
        "**": lambda: a ** b,
        "//": lambda: a // b,
        "%": lambda: a % b
    }

    return operations[letter]()

T = int(input())

for test_case in range(1, 1 + T):
    code = list(map(str, input().split()))
    stack = []
    result = 1

    for i in range(len(code)):
        if code[i] == ".":
            break

        try:
            stack.append(int(code[i]))
        except ValueError:
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                stack.append(operator(a, b, code[i]))
            else:
                result = 0
                break

    if result == len(stack) == 1:
        result = int(stack[0])
    else:
        result = "error"

    print(f'#{test_case}', result)