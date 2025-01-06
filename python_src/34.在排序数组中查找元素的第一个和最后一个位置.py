#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import *


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0: return [-1, -1]
        if size == 1: return [-1, -1] if target != nums[0] else [0, 0]

        l, r = 0, size - 1
        while l < r and r < size:
            mid = (l + r) << 1
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                pass
        
# @lc code=end

s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(s.searchRange(nums = [], target = 0))
