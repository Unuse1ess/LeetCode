#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import *

class Solution0:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp0: List[int] = triangle[-1].copy()
        dp1: List[int] = triangle[-1].copy()
        
        for line in reversed(triangle[:-1]):
            for i, n in enumerate(line):
                # dp1[i] = min(dp0[i], dp0[i + 1]) + n
                dp1[i] = (dp0[i] if dp0[i] < dp0[i + 1] else dp0[i + 1]) + n
                dp0 = dp1

        return dp1[0]
        
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += triangle[i + 1][j] if triangle[i + 1][j] < triangle[i + 1][j + 1] else triangle[i + 1][j + 1]
        
        return triangle[0][0]
# @lc code=end

s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(s.minimumTotal([[-10]]))
