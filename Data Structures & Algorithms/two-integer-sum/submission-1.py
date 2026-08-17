class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            n1 = target - nums[i]

            if n1 in seen:
                return [seen[n1], i]

            seen[nums[i]] = i