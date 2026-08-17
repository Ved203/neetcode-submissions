class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 =set(nums)
        if len(nums) == len(set1):
            return False
        else:
            return True