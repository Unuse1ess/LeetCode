#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import *
from cachetools import *

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        nums.append(nums[-1] + 1 if nums[-1] + 1 > target else target)
        while l <= r:
            mid = (l + r) >> 1
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return l + (1 if nums[l] < target else 0)
# @lc code=end

s = Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))
print(s.searchInsert(nums = [1,3,5,6], target = 2))
print(s.searchInsert(nums = [1,3,5,6], target = 7))
print(s.searchInsert(nums = [1,3,5,60], target = 6))
print(s.searchInsert([3,5,7,9,10], 8))
print(s.searchInsert([2,3,4,7,8,9], 11))
