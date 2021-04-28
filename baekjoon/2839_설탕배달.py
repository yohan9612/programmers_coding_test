# dp

n = int(input())

dp = [5001] * 5001
dp[3] = 1
dp[5] = 1

for i in range(5, n + 1):
    dp[i] = min(dp[i], dp[i - 3] + 1, dp[i - 5] + 1)

if dp[n] == 5001:
    dp[n] = -1
print(dp[n])

# greedy

# n = int(input())

# count = 0
# while n >= 0:
#     if n % 5 == 0:
#         count += n // 5
#         print(count)
#         break
#     n -= 3
#     count += 1
# else:
#     print(-1)
