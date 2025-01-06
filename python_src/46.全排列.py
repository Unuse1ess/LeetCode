#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import *
from itertools import *

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
        # visited: Set[int] = set()
        # size = len(nums)
        # res: List[List[int]] = []
        # tmp: List[int] = []

        # def dfs():
        #     if len(tmp) == size:
        #         res.append(tmp.copy())
        #         return
        #     for j in range(size):
        #         if j in visited: continue
        #         visited.add(j)
        #         tmp.append(nums[j])
        #         dfs()
        #         tmp.pop()
        #         visited.remove(j)
        # dfs()
        # return res
                
        
# @lc code=end

s = Solution()
print(s.permute(list(range(1, 4))))
print(s.permute(list(range(2))))
print(s.permute([1]))
