def factorial(n):
    if n == 0 or n == 1:
        return 1
    if dp[n - 1] != 0:
        dp[n] = n * dp[n - 1]
        return dp[n]
    dp[n] = n * factorial(n - 1)
    return dp[n]


def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


t = int(input())

dp = [0] * 31
dp[0] = 1
dp[1] = 1

answer = []
for _ in range(t):
    r, n = map(int, input().split())
    answer.append(combination(n, r))

for i in range(t):
    print(answer[i])
