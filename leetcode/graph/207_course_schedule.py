from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):

        if numCourses <= 1 or not prerequisites:
            return True

        graph = defaultdict(list)
        for k, v in prerequisites:
            graph[k].append(v)

        traced, visited = set(), set()

        def dfs(x):
            if x in traced:
                return False
            if x in visited:
                return True

            traced.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False

            traced.remove(x)
            visited.add(x)
            return True

        for i in list(graph):
            if not dfs(i):
                return False

        return True


s = Solution()

numCourses1 = 2
prerequisites1 = [[1, 0]]
print(s.canFinish(numCourses1, prerequisites1))

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
print(s.canFinish(numCourses2, prerequisites2))

numCourses2 = 20
prerequisites2 = [[0, 10], [3, 18], [5, 5], [
    6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
print(s.canFinish(numCourses2, prerequisites2))
