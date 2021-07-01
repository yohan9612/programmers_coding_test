def solution(n):
    map = [[0 for j in range(i, 0, -1)] for i in range(n, 0, -1)]

    dx = [1, -1, 0]
    dy = [-1, 0, 1]

    x, y = -1, len(map[0])
    num = 1

    for i in range(n):
        for _ in range(i, n):
            x += dx[i % 3]
            y += dy[i % 3]

            map[x][y] = num
            num += 1

    return sum(map, [])


print(solution(3))  # 5 6 1 4 2 3
print(solution(4))  # 7 8 9 1 6 10 2 5 3 4
