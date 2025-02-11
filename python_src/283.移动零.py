#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import *

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        l, r = 0, 0

        while r < N:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums
            
# @lc code=end

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([0]))

print(s.moveZeroes([0,0,0,32,1,0,3,12]))
print(s.moveZeroes([0,0,0,32,1,0,3,12,0,0]))
print(s.moveZeroes([32,1,0,3,12,0,0]))
print(s.moveZeroes([0,0]))