class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max = cur_min = 1

        for n in nums:
            candidates = (n, n * cur_max, n * cur_min)
            cur_max = max(candidates)
            cur_min = min(candidates)
            res = max(res, cur_max)

        return res