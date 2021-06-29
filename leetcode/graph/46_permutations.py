class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        prev_list = []

        def dfs(l):
            if len(l) == 0:
                answer.append(prev_list[:])

            for i in range(len(l)):
                next_list = l[:]
                next_list.remove(l[i])

                prev_list.append(l[i])
                dfs(next_list)
                prev_list.pop()

        dfs(nums)
        return answer
