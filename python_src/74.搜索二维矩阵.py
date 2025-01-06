#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
from typing import *

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        w, h = len(matrix[0]), len(matrix)
        get_pos = lambda x: (x // w, x % w)
        size = w * h

        l, r = 0, size
        while l <= r:
            mid = (l + r) >> 1
            x, y = get_pos(mid)
            if x < h and y < w:
                if target < matrix[x][y]:
                    r = mid - 1
                elif target > matrix[x][y]:
                    l = mid + 1
                else:
                    return True
            else:
                break
        return False

# @lc code=end

s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = -1))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 1))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 60))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 600))
