#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import *

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1
        dist = nums[0]
        i = 1
        while i <= dest and i <= dist:
            tmp = i + nums[i]
            dist = dist if dist > tmp else tmp
            i += 1
        return dist >= dest
# @lc code=end

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
