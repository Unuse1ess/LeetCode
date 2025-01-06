#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
from typing import *

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix)
        w = len(matrix[0])
        ret = [0 for _ in range(w * h)]
        end = [w, h, 0, 1]

        idx = 1
        dirct = 0
        pos = [0, 0]
        opt = [lambda x: x + 1, lambda x: x - 1]
        comp = [lambda a, b: a < b, lambda a, b: a >= b]
        cnt = 0
        while cnt < w * h:
            if comp[dirct // 2](pos[idx], end[dirct]):
            # if pos[idx] < end[dirct]:
                ret[cnt] = matrix[pos[0]][pos[1]]
                pos[idx] = opt[dirct // 2](pos[idx])
                cnt += 1
            else:
                end[dirct] = opt[dirct // 2 ^ 1](end[dirct])
                pos[idx] = opt[dirct // 2 ^ 1](pos[idx])
                idx ^= 1
                dirct = (dirct + 1) % 4
                pos[idx] = opt[dirct // 2](pos[idx])

        return ret
# @lc code=end

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(s.spiralOrder([[1]]))
print(s.spiralOrder([[1]] * 4))
print(s.spiralOrder([[1] * 4]))
