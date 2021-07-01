from collections import defaultdict


class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for k, v in sorted(tickets, reverse=True):
            graph[k].append(v)
        # for k, v in sorted(tickets):
        #     graph[k].append(v)

        # answer = []

        # def dfs(k):
        #     while graph[k]:
        #         dfs(graph[k].pop())
        #     answer.append(k)

        # dfs('JFK')
        # return answer[::-1]

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]


s = Solution()
print(s.findItinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"],
      ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
