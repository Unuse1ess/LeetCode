#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List
from collections import *

# @lc code=start
class Solution0:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        m = Counter(map(lambda t: t[1] - t[0], enumerate(sorted(set(nums)))))
        return max(m[k] for k in m)

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        max_cnt = 1
        for n in nums_set:
            if n - 1 not in nums_set:
                cnt = 1
                x = n
                while x + 1 in nums_set:
                    cnt += 1
                    x += 1
                max_cnt = cnt if cnt > max_cnt else max_cnt

        return max_cnt
# @lc code=end

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1,2,0,1]))
print(s.longestConsecutive([]))
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
print(s.longestConsecutive(list(range(2)) + list(range(-6, -2))))
