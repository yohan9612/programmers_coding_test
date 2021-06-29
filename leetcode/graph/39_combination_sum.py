class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #         answer = []

        #         def dfs(elements, index):
        #             s = sum(elements)
        #             if s == target:
        #                 answer.append(elements[:])
        #                 return
        #             elif s > target:
        #                 return

        #             for i in range(index, len(candidates)):
        #                 elements.append(candidates[i])
        #                 dfs(elements, i)
        #                 elements.pop()

        #         dfs([], 0)
        #         return answer

        answer = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            elif csum == 0:
                answer.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return answer
