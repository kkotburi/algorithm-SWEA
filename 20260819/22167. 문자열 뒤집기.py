T = int(input())

for _ in range(1, T + 1):
    letters = input()
    letters_reversed = ""
    index = len(letters) - 1

    while index >= 0:
        letters_reversed += letters[index]
        index -= 1

    print(letters_reversed)