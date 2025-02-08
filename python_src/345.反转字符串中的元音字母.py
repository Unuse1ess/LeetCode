#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
from typing import *

# @lc code=start
class Solution:
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    def reverseVowels(self, s: str) -> str:
        N = len(s)
        s = list(s)
        l, r = 0, N - 1
        while True:
            while l < N and s[l] not in Solution.vowels:
                l += 1
            while r >= 0 and s[r] not in Solution.vowels:
                r -= 1
            if l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                break
        return ''.join(s)
# @lc code=end

s = Solution()
print(s.reverseVowels("IceCreAm"))
print(s.reverseVowels("leetcode"))