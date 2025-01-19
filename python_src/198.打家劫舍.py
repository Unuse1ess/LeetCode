#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import *

class Solution0:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        dp = [None] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]
        
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, n):
            dp = nums[i] + dp0
            if dp1 > dp: dp = dp1
            
            dp0 = dp1
            dp1 = dp

        return dp1

# @lc code=end

s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
