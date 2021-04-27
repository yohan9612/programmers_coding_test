# 첫 번째 줄에 얼음틀의 세로 길이 N과 가로 길이 M이 주어짐.
# 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어짐.
# 구멍이 있으면 0, 그렇지 않으면 1

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
