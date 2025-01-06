#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        size = len(nums)
        if size == 0:
            return []

        ret = [[nums[0], nums[0]]]
        for n in nums[1:]:
            if n - ret[-1][-1] == 1:
                ret[-1][-1] = n
            else:
                ret.append([n, n])

        return [f"{i}->{j}" if i != j else str(i) for i, j in ret]
                
# @lc code=end

s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))
print(s.summaryRanges([9]))
print(s.summaryRanges([]))
