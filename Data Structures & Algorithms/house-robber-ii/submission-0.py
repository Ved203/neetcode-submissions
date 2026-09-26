class Solution:
    def rob(self, nums: List[int]) -> int:
        # prev2: Maximum money from two houses back.
        # prev1: Maximum money from the previous house.
        def rob_liner(arr):
            n= len(arr)

            if n==1:
                return arr[0]

            dp = n*[0]
            dp [0] = arr[0]
            dp [1] = max(arr[0], arr[1])

            for i in range(2,n):
                dp[i]=max(
                    dp[i-1],
                    dp[i-2]+arr[i]
                )
            return dp[n-1] 

        if len(nums) == 1:
            return nums[0]


        case1 = rob_liner(nums[:-1])
        case2 = rob_liner(nums[1:])

        return max(case1, case2)
