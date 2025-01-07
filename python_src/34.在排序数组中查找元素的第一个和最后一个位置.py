#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import *
from math import *

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0: return [-1, -1]
        if size == 1: return [-1, -1] if target != nums[0] else [0, 0]

        l, r = 0, size - 1
        step = size
        while l <= r and r < size:
            step >>= 1
            mid = (l + r) >> 1
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                if step == 0:
                    return mid, mid
                l, r = mid, mid
                prev = -1
                while True:
                    _l = l - step
                    if _l < 0: _l = 0
                    if nums[_l] == target:
                        l = _l
                    _r = r + step
                    if _r >= size: _r = size - 1
                    if nums[_r] == target:
                        r = _r
                    if step == 1 and r - l == prev:
                        break
                    prev = r - l
                    step = (step >> 1) | (step & 1)
            
                return l, r
        return -1, -1
# @lc code=end

s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(s.searchRange(nums = [], target = 0))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 7))
print(s.searchRange(nums = [5,7,7,8,8,8], target = 8))
print(s.searchRange(nums = [5,7,7,8,8,10,10], target = 10))
print(s.searchRange(nums = [5,5,7,8,8,8,10], target = 5))

## [15,20]
print(s.searchRange([1,1,1,2,4,4,4,5,5,5,5,6,7,8,8,9,9,9,9,9,9,10], 9))
