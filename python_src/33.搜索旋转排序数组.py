#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import *

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 1: return 0 if target == nums[0] else -1

        def bi_search(left: int, right: int) -> int:
            while left < right:
                mid = (left + right) >> 1
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    return mid
            if left == right and right != size:
                return left if nums[left] == target else -1
            return -1

        l, r = 0, size - 1
        res = -1
        while l < r and res == -1:
            mid = (l + r) >> 1
            d0 = nums[mid] - nums[l]
            d1 = nums[r] - nums[mid]

            if d0 >= 0 and d1 >= 0:
                return bi_search(l, r)
            if d0 >= 0:
                tmp = bi_search(l, mid)
                if tmp != -1:
                    return tmp
                l = mid + 1
                continue

            tmp = bi_search(mid, r)
            if tmp != -1:
                return tmp
            r = mid - 1

        if l == r and r != size:
            return l if nums[l] == target else -1
        return res

# @lc code=end

s = Solution()
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))
print(s.search(nums = [4,5,6,7,0,1,2], target = 3))
print(s.search(nums = [1], target = 0))
# nums = [4,5,6,7,0,1,2]
# for i in nums:
#     print(s.search(nums, i))

# nums = [4,5,-2,-1,0,1,2]
# for i in nums:
#     print(s.search(nums, i))

# print(s.search([3,1], 1))