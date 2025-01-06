#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in table:
                return [table[diff], i]
            table[n] = i
# @lc code=end

s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
print(s.twoSum(nums = [3,2,4], target = 6))
print(s.twoSum(nums = [3,3], target = 6))

