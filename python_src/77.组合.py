#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import *
from itertools import *

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))
        # return list(map(list, combinations(range(1, n + 1), k)))
# @lc code=end
        
class Solution0:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # if k == 1: return [[n]]

        res: List[List[int]] = []
        nums: List[int] = []

        def dfs(i: int):
            if len(nums) == k:
                res.append(nums.copy())
                return
            for j in range(i, n + 1):
                nums.append(j)
                dfs(j + 1)
                nums.pop()
        dfs(1)
        return res


s = Solution()
print(s.combine(n = 4, k = 2))
print(s.combine(n = 1, k = 1))
print(s.combine(n = 4, k = 3))
