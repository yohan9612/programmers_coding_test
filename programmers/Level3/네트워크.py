def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if i != j and computers[i][j] == 1 and visited[j] == False:
                dfs(j)

    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer
