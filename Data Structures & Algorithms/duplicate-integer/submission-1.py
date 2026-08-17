class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 =set(nums)
        if len(nums) == len(set1):
            return False
        else:
            return True

        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        # num1=[]
        # for i in nums:
        #     if i in num1:
        #         return True
        #     num1.append(i)
        # return False

        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False