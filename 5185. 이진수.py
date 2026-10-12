import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# for test_case in range(1, T + 1):
#     N, hex_str = input().split()
#     bin_str = ""

#     for char in hex_str:
#         bin_str += format(int(char, 16), '04b')

#     print(f'#{test_case}', bin_str)


# GPT 활용
# for ts in range(1, T + 1):
#     N, hex_str = input().split()
#     bin_str = ''.join(f'{int(char, 16):04b}' for char in hex_str)
#     print(f'#{ts} {bin_str}')


# 교재 진법 변환
# for test_case in range(1, T + 1):
#     N, hex_str = input().split()
#     result = []

#     for char in hex_str:
#         dec = int(char, 16)
#         bin_str = ''

#         for _ in range(4):
#             bin_str = str(dec % 2) + bin_str
#             dec //= 2

#         result.append(bin_str)

#     print(f'#{test_case}', ''.join(result))


# 교재 비트 연산
for test_case in range(1, T + 1):
    N, hex_str = input().split()
    result = []

    for char in hex_str:
        value = int(char, 16)
        bin_str = ''

        for j in range(3, -1, -1):
            bin_str += '1' if value & (1 << j) else '0'
                
        result.append(bin_str)

    print(f'#{test_case}', ''.join(result))


import ctypes
print(ctypes.c_int8(255).value)