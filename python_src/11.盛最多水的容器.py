#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import *

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        l, r = 0, size - 1
        # l0, r0 = 0, size
        lmax, rmax = height[l], height[r]
        cap = 0
        while l < r:
            h = lmax if lmax < rmax else rmax
            cap0 = h * (r - l)
            cap = cap if cap > cap0 else cap0
            if height[l] < height[r]:
                l += 1
                # lmax = max(lmax, height[l])
                lmax = lmax if lmax > height[l] else height[l]
            else:
                r -= 1
                # rmax = max(rmax, height[r])
                rmax = rmax if rmax > height[r] else height[r]

        return cap

# @lc code=end

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
