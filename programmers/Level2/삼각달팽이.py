def solution(n):
    map = [[0 for j in range(i + 1)] for i in range(n)]

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            x += dx[i % 3]
            y += dy[i % 3]

            map[x][y] = num
            num += 1

    return sum(map, [])


print(solution(4))  # [1,2,9,3,10,8,4,5,6,7]
print(solution(5))  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6))  # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
