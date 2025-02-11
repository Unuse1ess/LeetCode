#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#
from typing import *

# @lc code=start
class Solution:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    def maxVowels(self, s: str, k: int) -> int:
        nums = [c in Solution.vowels for c in s]
        N = len(nums)
        s = sum(nums[:k])
        max_s = s
        for i in range(k, N):
            s += nums[i] - nums[i - k]
            if s > max_s: max_s = s
        return max_s
        
# @lc code=end

s = Solution()
print(s.maxVowels("abciiidef", 3))
print(s.maxVowels("aeiou", 2))
print(s.maxVowels("leetcode", 3))
print(s.maxVowels("rhythms", 4))
print(s.maxVowels("tryhard", 4))
