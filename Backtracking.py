# def backtrack(now, n, stack):
#     if now == n:
#         print(stack)

#     else:
#         candidates = [0] * n
#         count = make_candidates(now, n, stack, candidates)
#         for i in range(count):
#             stack[now] = candidates[i]
#             backtrack(now + 1, n, stack)

# def make_candidates(now, n, stack, candidates):
#     used = [False] * (n + 1)
#     count = 0

#     for i in range(now):
#         used[stack[i]] = True

#     for i in range(1, n + 1):
#         if not used[i]:
#             candidates[count] = i
#             count += 1

#     return count

# n = 3
# stack = [0] * n
# backtrack(0, n, stack)

def backtrack(position, n, stack):
    # 모든 자리에 숫자를 채우면 출력
    if position == n:
        return print(stack)

    # 현재 위치에 넣을 수 있는 숫자 찾기
    candidates = make_candidates(position, n, stack)
    print("여기", position, candidates)

    # 후보 숫자를 하나씩 선택
    for number in candidates:
        stack[position] = number
        backtrack(position + 1, n, stack) 


def make_candidates(position, n, stack):
    used = [False] * (n + 1)

    # 이미 사용한 숫자 체크
    for i in range(position):
        used[stack[i]] = True

    # 사용하지 않은 숫자만 후보로 반환
    candidates = []
    for number in range(1, n + 1):
        if not used[number]:
            candidates.append(number)

    return candidates


n = 3
stack = [0] * n
backtrack(0, n, stack)