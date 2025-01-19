#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
from typing import *

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp0 = 1
        dp1 = 1

        for _ in range(2, n + 1):
            # dp[i] = dp[i - 1] + dp[i - 2]

            dp = dp0 + dp1
            dp0 = dp1
            dp1 = dp

        return dp1
# @lc code=end

s = Solution()
print([s.climbStairs(i) for i in range(1, 46)])
