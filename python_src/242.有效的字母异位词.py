#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = ord('a')
        hist = [0 for i in range(a + 26)]
        for c in map(ord, s):
            hist[c] += 1
        for c in map(ord, t):
            hist[c] -= 1
        return all(i == 0 for i in hist[a:])
# @lc code=end

s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))
print(s.isAnagram(s = "rat", t = "car"))
print(s.isAnagram(s = "aacc", t = "ccac"))
print(s.isAnagram(s = "ab", t = "a"))
