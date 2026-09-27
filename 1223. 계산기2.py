import sys
sys.stdin = open("input.txt", "r")

# GPT
for test_case in range(1, 11):
    n = int(input())
    cal_str = input()
    cal_list = []
    operators = []

    for char in cal_str:
        if char.isdigit():
            cal_list.append(char)
        else:
            if char == "+":
                while operators:
                    cal_list.append(operators.pop())
            operators.append(char)

    while operators:
        cal_list.append(operators.pop())

    nums = []

    for char in cal_list:
        if char.isdigit():
            nums.append(int(char))
        elif char == "+":
            nums.append(nums.pop() + nums.pop())
        elif char == "*":
            nums.append(nums.pop() * nums.pop())

    print(f'#{test_case}', nums[0])