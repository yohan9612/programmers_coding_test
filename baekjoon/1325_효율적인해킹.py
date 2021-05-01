import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    global count
    count += 1
    print(v, end=' ')
    for i in range(1, len(graph[v])):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b][a] = 1

answer = []
count = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i)
    answer.append(count)
    count = 0
    print()

# for i in range(len(answer)):
#     if answer[i] == max(answer):
#         print(i + 1, end=' ')
