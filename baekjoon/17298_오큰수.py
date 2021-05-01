from collections import deque

n = int(input())
nums = list(map(int, input().split()))

q = deque()

answer = [-1] * n


def nge():
    for i in range(n):
        while q and q[-1][0] < nums[i]:
            tmp, idx = q.pop()
            print(q, q[-1], q[-1][0], tmp, idx)
            answer[idx] = nums[i]
        q.append([nums[i], i])


nge()

print(*answer)
