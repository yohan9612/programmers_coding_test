num = int(input())

if num % 2 == 0:
    print('CY')
else:
    print('SK')

# SK or CY
# 1개 혹은 3개
# f(n) = max(sum(n_{i - 1}, n_{i + 1}))

# 5개     SK    CY
#         1     1
#         1     1
#         1

#         1     3
#         1

#         3     1
#         1

# n이 짝수개면 CY, 홀수개면 SK
