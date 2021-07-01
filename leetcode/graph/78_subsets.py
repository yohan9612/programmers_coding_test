class Solution:
    def subsets(self, nums):
        answer = []

        def dfs(index, path):
            answer.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return answer


nums1 = [0]
nums2 = [1, 2, 3]
s = Solution()
print(s.subsets(nums1))
print(s.subsets(nums2))
