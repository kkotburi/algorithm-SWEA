import sys
sys.stdin = open("input.txt", "r")


DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    energies = []

    for _ in range(N):
        x, y, d, e = map(int, input().split())
        energies.append([x * 2, y * 2, d, e])

    result = 0
    count = 2000

    while energies and count:

        for energy in energies:
            x, y, d, e = energy
            energy[0] = x + DIRECTIONS[d][0]
            energy[1] = y + DIRECTIONS[d][1]

        for i in range(N):
            is_pop = False
            for j in range(i + 1, N):
                if energies[j] and energies[j][0] == energies[i][0] and energies[j][1] == energies[i][1]:
                    result += energies[j][3]
                    energies[j] = False
                    is_pop = True
            if is_pop:
                result += energies[i][3]
                energies[i] = False

        # k = 0
        # while k < len(energies):
        #     is_pop = False
        #
        #     l = k + 1
        #     while l < len(energies):
        #         if energies[k][0] == energies[l][0] and energies[k][1] == energies[l][1]:
        #             result += energies[l][3]
        #             energies.pop(l)
        #             l -= 1
        #             is_pop = True
        #         l += 1
        #
        #     if is_pop:
        #         result += energies[k][3]
        #         energies.pop(k)
        #         k -= 1
        #
        #     k += 1

        count -= 1

    print(f'#{tc} {result}')


# 풀이 참고
# for tc in range(1, T + 1):
#     N = int(input())
#     energies = []

#     for _ in range(N):
#         x, y, d, e = map(int, input().split())
#         energies.append([x * 2, y * 2, d, e])

#     result = 0

#     while N:
#         tmp = []
#         positions = set()
#         collisions = set()

#         for energy in energies:
#             x, y, d, e = energy

#             nx = x + DIRECTIONS[d][0]
#             ny = y + DIRECTIONS[d][1]

#             energy[0] = nx
#             energy[1] = ny

#             if (nx, ny) in positions:
#                 collisions.add((nx, ny))
#             else:
#                 positions.add((nx, ny))

#         for x, y, d, e in energies:
#             if (x, y) in collisions:
#                 result += e
#                 N -= 1

#             elif x < -2000 or x > 2000 or y < -2000 or y > 2000:
#                 N -= 1

#             else:
#                 tmp.append([x, y, d, e])

#         energies = tmp

#     print(f'#{tc} {result}')