import collections


def solution(bridge_length, weight, truck_weights):
    q = collections.deque()
    for t in truck_weights:
        q.append(t)
    dis = []
    truck_len = len(truck_weights)
    time = 0
    dis, crossed, crossing = collections.deque(
    ), collections.deque(), collections.deque()
    while len(crossed) != truck_len:
        if dis and dis[0] == bridge_length:
            crossed.append(crossing.popleft())
            dis.popleft()
        if q and sum(crossing, q[0]) <= weight:
            crossing.append(q.popleft())
            dis.append(0)
        for i in range(len(dis)):
            dis[i] += 1
        time += 1
    return time


print(solution(2, 10, [7, 4, 5, 6]))
