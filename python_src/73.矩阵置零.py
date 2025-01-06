#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
from typing import *

class Solution0:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()

        h = len(matrix)
        w = len(matrix[0])
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for r in row:
            for i in range(w):
                matrix[r][i] = 0
        for c in col:
            for i in range(h):
                matrix[i][c] = 0
        
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])

        row = False
        col = False
        for i in range(w):
            if matrix[0][i] == 0:
                row = True
                break
        for i in range(h):
            if matrix[i][0] == 0:
                col = True
                break

        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row:
            for i in range(w):
                matrix[0][i] = 0
        if col:
            for i in range(h):
                matrix[i][0] = 0
# @lc code=end

s = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print('\n'.join(str(i) for i in matrix))
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print('\n'.join(str(i) for i in matrix))
matrix = [[1, 0, 3]]
s.setZeroes(matrix)
print('\n'.join(str(i) for i in matrix))
matrix = [[1], [0], [3]]
s.setZeroes(matrix)
print('\n'.join(str(i) for i in matrix))
