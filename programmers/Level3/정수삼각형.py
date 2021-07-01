def solution(triangle):

    dp_table = [[0 for _ in range(len(triangle[i]))]
                for i in range(len(triangle))]

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                dp_table[i][j] = triangle[i][j]
            elif j == 0:
                dp_table[i][j] = triangle[i][j] + dp_table[i - 1][j]
            elif j == len(triangle[i]) - 1:
                dp_table[i][j] = triangle[i][j] + dp_table[i - 1][j - 1]
            else:
                dp_table[i][j] = triangle[i][j] + \
                    max(dp_table[i - 1][j], dp_table[i - 1][j - 1])

    return max(dp_table[-1])
