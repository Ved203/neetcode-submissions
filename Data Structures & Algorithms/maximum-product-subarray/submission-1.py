# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         res = nums[0]
#         cur_max = cur_min = 1

#         for n in nums:
#             candidates = (n, n * cur_max, n * cur_min)
#             cur_max = max(candidates)
#             cur_min = min(candidates)
#             res = max(res, cur_max)

#         return res


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp_max = max(n, n * cur_max, n * cur_min)
            temp_min = min(n, n * cur_max, n * cur_min)

            cur_max = temp_max
            cur_min = temp_min

            res = max(res, cur_max)

        return res