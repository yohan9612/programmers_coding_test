def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return dp[n]


t = int(input())
nums = []
for _ in range(t):
    nums.append(int(input()))
dp = [0] * 41

for i in range(len(nums)):
    fibonacci(nums[i])
    if nums[i] == 0:
        print(1, 0)
    elif nums[i] == 1:
        print(0, 1)
    else:
        print(fibonacci(nums[i] - 1), fibonacci(nums[i]))
