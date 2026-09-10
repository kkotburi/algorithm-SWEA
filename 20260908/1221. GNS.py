T = int(input())

for _ in range(1, T + 1):
    test_case, n = map(str, input().split())
    nums = list(map(str, input().split()))
    result = []

    num_dict = {
        "ZRO": 0,
        "ONE": 0,
        "TWO": 0,
        "THR": 0,
        "FOR": 0,
        "FIV": 0,
        "SIX": 0,
        "SVN": 0,
        "EGT": 0,
        "NIN": 0
    }

    for num in nums:
        num_dict[num] += 1

    for key, value in num_dict.items():
        for _ in range(value):
            result.append(key)

    print(f'{test_case}\n{" ".join(result)}')
