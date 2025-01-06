#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from typing import *

# x' = xcos(a) - ysin(a)
# y' = xsin(a) + ycos(a)

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix)
        mid = w / 2 - 0.5
        for i in range(w):
            for j in range(w):
                if i <= j:
                    continue
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp
        # print(matrix)
        for i in range(w):
            for j in range(w >> 1):
                j0 = int(2 * mid - j)
                tmp = matrix[i][j0]
                matrix[i][j0] = matrix[i][j]
                matrix[i][j] = tmp
        # print(matrix)
# @lc code=end

s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
