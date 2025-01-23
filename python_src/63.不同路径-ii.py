#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import *
from functools import *

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp: List[int] = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[n - 1]

# @lc code=end

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))

## 0
print(s.uniquePathsWithObstacles([[0,0],[0,1]]))

## 0
print(s.uniquePathsWithObstacles([[1,0]]))

## 0
print(s.uniquePathsWithObstacles([[0,1,0,0]]))