#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#
from typing import *
from collections import *


# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter(map(tuple, grid))
        return sum(cnt[col] for col in zip(*grid))
# @lc code=end

class Solution0:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r_set = Counter(map(tuple, grid))
        c_set = Counter(zip(*grid))
        ret = 0
        for key in r_set.keys() & c_set.keys():
            ret += r_set[key] * c_set[key]
        return ret

class Solution1:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        cnt = Counter(tuple(r) for r in grid)
        ret = 0
        for i in range(N):
            ret += cnt[tuple(grid[j][i] for j in range(N))]
        return ret

s = Solution()
print(s.equalPairs(grid=[[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(s.equalPairs(grid=[[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))

print(s.equalPairs(grid=[[3, 3, 2, 2], [3, 3, 4, 5], [2, 2, 2, 2], [2, 2, 1, 2]]))
