
# 26 - 1
# 25 / 5
# 5 / 5

# a_i = min(a_{i - 1}, a_{i / 2}, a_{i / 3}, a_{i / 5}) + 1

x = int(input())

dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])
