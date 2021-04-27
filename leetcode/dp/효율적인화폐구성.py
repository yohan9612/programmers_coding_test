n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))

dp = [10001] * (m + 1)

dp[0] = 0
for i in range(n):
    for j in range(nums[i], m + 1):
        if dp[j - nums[i]] != 10001:
            dp[j] = min(dp[j], dp[j - nums[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
