import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

answer = {}


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            answer[i] = v
            dfs(i)


dfs(1)
for i in range(2, n + 1):
    if i in answer:
        print(answer[i])
