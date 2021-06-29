class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                answer.append(prev_elements[:])

            for i in range(len(elements)):
                next_elements = elements[:]
                next_elements.remove(elements[i])

                prev_elements.append(elements[i])
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return answer
