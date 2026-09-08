import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# for test_case in range(1, T + 1):
#     str_dict = {}
#     for key in "".join(input()):
#         str_dict[key] = 0
#     for letter in "".join(input()):
#         if letter in str_dict:
#             str_dict[letter] += 1
#
#     max = 0
#     for letter in str_dict:
#         if str_dict[letter] > max:
#             max = str_dict[letter]

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    max = 0

    for letter1 in str1:
        count = 0
        for letter2 in str2:
            if letter2 == letter1:
                count += 1

        if count > max:
            max = count

    print(f'#{test_case}', max)