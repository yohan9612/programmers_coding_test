# n * m 크기의 금광이 있음.
# 첫 번쨰 열부터 금을 캐기 시작. 처음에는 첫 째 열의 어느 행에서든 출발 가능.
# m - 1번에 걸쳐 매번 오른쪽위, 오른쪽, 오른쪽 아래 세가지 중 하나로 이동해야 함.
# 채굴자가 얻을 수 있는 금의 최대 크기는?

# dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

for t in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
