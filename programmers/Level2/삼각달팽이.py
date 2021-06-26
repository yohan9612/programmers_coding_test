def solution(n):
    map = [[0 for i in range(1, j + 1)] for j in range(1, n + 1)]
    
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            map[x][y] = num
            num += 1

    return sum(map, [])
