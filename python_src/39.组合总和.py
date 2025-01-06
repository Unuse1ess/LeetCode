#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import *

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[Tuple[int]] = []
        tmp: List[int] = []
        size = len(candidates)
        
        def dfs(i: int, s: int):
            if s == target:
                res.append(tmp[:])
                return
            elif s > target:
                return

            for j in range(i, size):
                tmp.append(candidates[j])
                dfs(j, s + candidates[j])
                tmp.pop()
        dfs(0, 0)
        return res
        
# @lc code=end

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
print(s.combinationSum([2], 1))
