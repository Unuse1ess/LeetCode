#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import *
from operator import *

class Solution0:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = nums[0]
        for n in nums[1:]:
            s = tmp + n
            tmp = n if s < n else s
            res = tmp if tmp > res else res
        return res

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # lsum, rsum, isum, msum
        def dq(l: int, r: int) -> Tuple[int, int, int, int]:
            size = r - l
            if size == 1:
                return (nums[l],) * 4
            mid = (l + r) >> 1
            lt = dq(l, mid)
            rt = dq(mid, r)
            
            isum = lt[2] + rt[2]
            lsum = max(lt[0], lt[2] + rt[0])
            rsum = max(rt[1], rt[2] + lt[1])

            return lsum, rsum, isum, max(lt[1] + rt[0], lt[3], rt[3])

        return dq(0, len(nums))[3]
# @lc code=end

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-2,1]))
