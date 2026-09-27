import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N - K + 1):
            if (j == 0 or not matrix[i][j - 1]) and (j + K == N or not matrix[i][j + K]):
                row_possible = True
                for k in range(K):
                    if not matrix[i][j + k]:
                        row_possible = False
                        break
                if row_possible:
                    result += 1

            if (j == 0 or not matrix[j - 1][i]) and (j + K == N or not matrix[j + K][i]):
                col_possible = True
                for k in range(K):
                    if not matrix[j + k][i]:
                        col_possible = False
                        break
                if col_possible:
                    result += 1

    print(f'#{test_case}', result)


# GPT
T = int(input())

def valid_blank(line, K):
    count = 0
    answer = 0

    for cell in line:
        if cell:
            count += 1
        else:
            if count == K:
                answer += 1
            count = 0

    if count == K:
        answer += 1

    return answer

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for row in matrix:
        result += valid_blank(row, K)
    for col in zip(*matrix):
        result += valid_blank(col, K)

    print(f'#{test_case}', result)