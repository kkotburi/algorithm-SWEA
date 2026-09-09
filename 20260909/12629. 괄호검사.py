import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    code = input()
    bracket_dict = {
        "}" : "{",
        ")" : "("
    }
    stack = [0]

    for letter in code:
        # if bracket_dict.get(letter) == stack[-1]:
        #     stack.pop()
        # elif letter == "}" or letter == ")":
        #     break
        # elif letter == "{" or letter == "(":
        #     stack.append(letter)
        if letter in bracket_dict.values():
            stack.append(letter)
        elif letter in bracket_dict:
            if bracket_dict.get(letter) == stack[-1]:
                stack.pop()
            else:
                stack[0] = 0
                break

    if len(stack) == 1:
        stack[0] = 1

    print(f'#{test_case}', stack[0])