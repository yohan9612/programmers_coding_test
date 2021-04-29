n, m = map(int, input().split())

visited = [False] * (n + 1)

graph = [0] * m


def dfs(i):
    if i == m:
        print(' '.join(map(str, graph)))
        return

    for j in range(1, n + 1):
        if not visited[j]:
            visited[j] = True
            graph[i] = j
            dfs(i + 1)
            visited[j] = False


dfs(0)
