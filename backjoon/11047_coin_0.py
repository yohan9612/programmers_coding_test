n, k = map(int, input().split())

coins = [int(input()) for x in range(n)]

tmp = k
count = 0

# while tmp != 0:
#     for i in range(n):
#         if coins[i] == tmp:
#             count += 1
#             tmp -= coins[i]
#             break
#         elif coins[i] > tmp:
#             count += 1
#             tmp -= coins[i - 1]
#             break

while tmp != 0:
    coin = coins.pop()
    count += tmp // coin
    tmp %= coin

print(count)
