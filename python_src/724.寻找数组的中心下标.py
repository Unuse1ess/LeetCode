#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#
from typing import *

class Solution0:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0

        p_sum = nums.copy()
        for i in range(1, N):
            p_sum[i] += p_sum[i - 1]
            nums[-i - 1] += nums[-i]

        if nums[1] == 0: return 0
        for i in range(1, N - 1):
            if p_sum[i - 1] == nums[i + 1]:
                return i
        if p_sum[-2] == 0: return N - 1
        return  -1
        
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0

        s_sum = sum(nums)
        p_sum = 0
        for i in range(N):
            s_sum -= nums[i]
            if p_sum == s_sum: return i
            p_sum += nums[i]
        return -1
# @lc code=end

s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([1, 2, 3]))
print(s.pivotIndex([2, 1, -1]))

print(s.pivotIndex([0,1]))
print(s.pivotIndex([1,0]))
