#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import *

class Solution0:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 1:
            return 0

        rain = 0
        right = height.copy()
        m = 0
        for i in range(size - 1, -1, -1):
            m = max(height[i], m)
            right[i] = m
        m = 0
        for h, r in zip(height, right):
            m = max(h, m)
            rain += min(m, r) - h

        return rain

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 1:
            return 0
        l, r = 0, size - 1
        lmax, rmax = 0, 0
        rain = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    rain += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    rain += rmax - height[r]
                r -= 1

        return rain
# @lc code=end

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
print(s.trap([3,1,1,1,10]))
