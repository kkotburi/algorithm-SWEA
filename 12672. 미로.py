import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    start = []
    end = []
    visited = {start}
    location = [start]


    print(n, matrix)