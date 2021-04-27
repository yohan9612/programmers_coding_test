n = int(input())
nums = list(map(int, input().split()))

dp = [0] * 100
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

print(dp[n - 1])
