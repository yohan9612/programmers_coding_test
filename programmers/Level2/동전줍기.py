def solution(map):

    dp_table = [[0 for _ in range(len(map[i]))] for i in range(len(map))]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if i < 1 and j < 1:
                dp_table[i][j] = map[i][j]
            elif i < 1 and j >= 1:
                dp_table[i][j] = map[i][j] + dp_table[i][j - 1]
            elif i >= 1 and j < 1:
                dp_table[i][j] = map[i][j] + dp_table[i - 1][j]
            else:
                dp_table[i][j] = map[i][j] + \
                    max(dp_table[i - 1][j], dp_table[i][j - 1],
                        dp_table[i - 1][j - 1])

    print(dp_table)
    return dp_table[-1][-1]


map1 = [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]  # 22
print(solution(map1))
map2 = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]  # 17
print(solution(map2))
