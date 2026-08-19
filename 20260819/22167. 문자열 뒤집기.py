T = int(input())
for test_case in range(1, T + 1):
    letters = input()
    letters_reverse = ""
    index = len(letters) - 1
    print(index)
    while index >= 0:
        letters_reverse += letters[index]
        index -= 1
    print(letters_reverse)