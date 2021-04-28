def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == '1':
        graph[x][y] = '0'
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        global count
        count += 1
        return True
    return False


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(str, input())))

answer, count, result = [], 0, 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(count)
            count = 0
            result += 1
print(result)
for i in range(len(answer)):
    print(sorted(answer)[i])
