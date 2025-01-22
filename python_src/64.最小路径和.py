#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import *
from functools import *

class Solution0:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i == m - 1 and j == n:
                return 0
            elif i == m or j == n:
                return 80000000
            a = dfs(i + 1, j)
            b = dfs(i, j + 1)
            if a < b: return a + grid[i][j]
            else: return b + grid[i][j]

        return dfs(0, 0)
    
# 状态转移方程（不考虑边界）为dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
# 转换成滚动数组后，dp本身在下一行为dp[i - 1][:]，不用两个1维数组。

# @lc code=start
class Solution:
    MAX = 80000000
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [Solution.MAX] * (n + 1)

        dp[0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j] = (dp[j] if dp[j] < dp[j - 1] else dp[j - 1]) + grid[i - 1][j - 1]
            dp[0] = Solution.MAX

        return dp[n]
# @lc code=end

s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))


## 5400
print(s.minPathSum([[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100],[100,100,100]]))
