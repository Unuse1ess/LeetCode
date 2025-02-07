#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from typing import *

class Solution0:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])

        size = 0
        dp = [[0] * (w + 1)] + [[0] + [int(matrix[i][j]) for j in range(w)] for i in range(h)]
        
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                if dp[i][j] > 0:
                    dp[i][j] = min(dp[i - 1][j - 1],
                                    dp[i - 1][j],
                                    dp[i][j - 1]) + 1
                    if dp[i][j] > size: size = dp[i][j]
        return size * size

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        h = len(matrix)
        w = len(matrix[0])

        size = 0
        dp = [[0] * (w + 1) for _ in range(h + 1)]
        
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1],
                                    dp[i - 1][j],
                                    dp[i][j - 1]) + 1
                    if dp[i][j] > size: size = dp[i][j]
        return size * size
# @lc code=end

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(s.maximalSquare([["0","1"],["1","0"]]))
print(s.maximalSquare([["0"]]))
