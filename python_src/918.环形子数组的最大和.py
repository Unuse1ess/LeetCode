#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#
from typing import *

class Solution0:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # lsum, rsum, isum, msum, csum
        def dq(l: int, r: int) -> Tuple[int, int, int, int, int]:
            size = r - l
            if size == 1:
                return (nums[l],) * 5
            mid = (l + r) >> 1
            lt = dq(l, mid)
            rt = dq(mid, r)
            
            isum = lt[2] + rt[2]
            lsum = max(lt[0], lt[2] + rt[0])
            rsum = max(rt[1], rt[2] + lt[1])
            msum = max(lt[1] + rt[0], lt[3], rt[3])
            csum = max(lt[2] + rt[4], rt[2] + lt[4], lt[0] + rt[1])

            return lsum, rsum, isum, msum, csum

        _, _, _, a, b = dq(0, len(nums))
        return a if a > b else b
        
# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res_max, res_min = nums[0], nums[0]
        tmp_max, tmp_min = nums[0], nums[0]
        sm = nums[0]
        for n in nums[1:]:
            s = tmp_max + n
            tmp_max = n if s < n else s
            res_max = tmp_max if tmp_max > res_max else res_max
            s = tmp_min + n
            tmp_min = n if s > n else s
            res_min = tmp_min if tmp_min < res_min else res_min
            sm += n
        s = sm - res_min
        return res_max if res_max > s or sm == res_min else s
# @lc code=end

s = Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2]))
print(s.maxSubarraySumCircular([5,-3,5]))
print(s.maxSubarraySumCircular([3,-2,2,-3]))
print(s.maxSubarraySumCircular([1,1,1,1,1,1,1,1,1,-100,1,1]))
print(s.maxSubarraySumCircular([-9,-8,-7]))
print(s.maxSubarraySumCircular([1,-6,-7,4]))
