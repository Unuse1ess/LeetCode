#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import *

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        l, r = 0, size - 1
        m = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                m = nums[l] if nums[l] < m else m
                return m

            mid = (l + r) >> 1
            if nums[mid] <= nums[r]:
                m = nums[mid] if nums[mid] < m else m
                r = mid - 1
            elif nums[l] <= nums[mid]:
                m = nums[l] if nums[l] < m else m
                l = mid + 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return m

# @lc code=end

s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([11,13,15,17]))
print(s.findMin([1,2,3,4,5,6,7,0]))
