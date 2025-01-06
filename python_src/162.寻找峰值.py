#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
from typing import *

class Solution0:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1: return 0
        if size == 2:
            return 0 if nums[0] > nums[1] else 1

        res = -1

        def dq(l: int, r: int, flag: bool) -> int:
            nonlocal res

            if res != -1: return 0

            _size = r - l
            if _size == 1:
                if l == -1 or l == 0:
                    return 1
                elif l == size:
                    return -1
                return nums[l] - nums[l - 1]
            if _size == 2:
                if l == size - 1:
                    return -1
                elif l == -1:
                    return 1
                return nums[l + 1] - nums[l]

            mid = (l + r) >> 1
            a = dq(l, mid, True)
            b = dq(mid, r, False)
            
            if res == -1 and a > 0 and b < 0:
                if mid == 0 or nums[mid - 1] < nums[mid]:
                    res = mid
                else:
                    res = mid - 1
                return 0

            if a == 0:
                return b
            elif b == 0:
                return a
            return b if flag else a


        dq(-1, size + 1, True)
        return res
        
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1: return 0
        if size == 2:
            return 0 if nums[0] > nums[1] else 1

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1

            d0 = nums[mid] - nums[mid - 1] if mid - 1 >= 0 else 1
            d1 = nums[mid + 1] - nums[mid] if mid + 1 < size else -1

            if d0 > 0 and d1 > 0:
                l = mid
            elif d0 > 0 and d1 < 0:
                return mid
            else:
                r = mid
                
# @lc code=end

s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([3,2,1]))
print(s.findPeakElement([1,2,3]))
print(s.findPeakElement([1,2,3,4,5]))
print(s.findPeakElement([5,4,3,2,1]))
print(s.findPeakElement([4,3,2,1,4]))
