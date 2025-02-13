#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from typing import *

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        l, r = 0, 0
        ret = 0
        while r < N:
            if nums[r] == 0:
                if k > 0:
                    k -= 1
                else:
                    k += not nums[l]
                    l += 1
                    continue
            tmp = r - l + 1
            if ret < tmp: ret = tmp
            r += 1
        return ret
        
# @lc code=end

s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,0], 3))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,0], 0))
print(s.longestOnes([0,0] * 3, 0))

print(s.longestOnes([0], 1))
print(s.longestOnes([0], 0))
print(s.longestOnes([1], 0))