import math

n = int(input())

dp = [50000] * (n + 1)
dp[1] = 1

for i in range(n + 1):
    if i == int(math.sqrt(i)) ** 2:
        dp[i] = 1

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[n])
