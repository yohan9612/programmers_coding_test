class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force
        """
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j

        """
        Search with 'in'
        """
        # for i, n in enumerate(nums):
        #     complement = target - n

        #     if complement in nums[i + 1:]:
        #         return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

        """
        Not search & compare
        """
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
