class Solution:
    def combinationSum(self, nums, target):
        result = []

        def backtrack(i,curr, remaining):
            # Found a valid combination
            if remaining == target:
                result.append(curr.copy())
                return

            # Target exceeded or no numbers left
            if remaining > target or i >= len(nums):
                return

            # Choose nums[i]
            curr.append(nums[i])
            backtrack(i,  curr, remaining + nums[i])

            # Don't choose nums[i]
            curr.pop()
            backtrack(i + 1,  curr, remaining)

        backtrack(0,  [], 0)

        return result