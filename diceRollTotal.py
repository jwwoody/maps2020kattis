
d = 3
f =6
target = 10

memo = {}

def dp(d, target):
    # print(memo)
    if d == 0:
        return 0 if target > 0 else 1
    if (d, target) in memo:
        return memo[(d, target)]
    to_return = 0
    for k in range(max(0, target-f), target):
        to_return += dp(d-1, k)
    memo[(d, target)] = to_return
    print(memo)
    return to_return
print(dp(d, target) % (10**9 + 7))