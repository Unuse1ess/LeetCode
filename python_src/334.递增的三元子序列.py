#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
from typing import *

# 参考最长递增子序列解法。
# 此实现使用了语言特性（空值None）。对于没有此特性的语言，变量a、b需要存放索引值。

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 3: return False

        a, b = nums[0], None

        for n in nums[1:]:
            if n <= a:
                a = n
            elif b is None:
                b = n
            elif n > b:
                return True
            elif n < b:
                b = n
        return False
# @lc code=end

s = Solution()
print(s.increasingTriplet(nums = [1,2,3,4,5]))
print(s.increasingTriplet(nums = [5,4,3,2,1]))
print(s.increasingTriplet(nums = [2,1,5,0,4,6]))

## false
print(s.increasingTriplet([1] * 194))

## false
print(s.increasingTriplet([1,2,1,2,1,2,1,2,1,2]))