#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#
from typing import *

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        
        k = 1
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

        return 0 if ret == 0 else ret - 1
# @lc code=end

s = Solution()
print(s.longestSubarray([1,1,0,1]))
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(s.longestSubarray([1,1,1]))

print(s.longestSubarray([0] * 4))