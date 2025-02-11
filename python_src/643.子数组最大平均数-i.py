#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
from typing import *

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        s = sum(nums[:k])
        max_s = s
        for i in range(k, N):
            s += nums[i] - nums[i - k]
            if s > max_s: max_s = s
        return max_s / k
        
# @lc code=end

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([5], 1))
