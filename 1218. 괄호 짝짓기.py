import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 2):
    n = int(input())
    brackets = input()
    bracket_dict = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
        ">" : "<"
    }
    validity = [0, brackets[0]]

    for i in range(1, n):
        if n % 2 or len(validity) - 1 > n - i:
            break

        if bracket_dict.get(brackets[i]) == validity[-1]:
            validity.pop()
        else:
            validity.append(brackets[i])

    if len(validity) == 1:
        validity[0] = 1

    print(f'#{test_case}', validity[0])