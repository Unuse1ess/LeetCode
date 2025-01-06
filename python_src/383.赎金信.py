#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hist = {}
        for c in magazine:
            hist[c] = hist.get(c, 0) + 1
        for c in ransomNote:
            if c in hist:
                hist[c] -= 1
                if hist[c] < 0:
                    return False
            else:
                return False
        return True
# @lc code=end

s = Solution()
print(s.canConstruct(ransomNote = "a", magazine = "b"))
print(s.canConstruct(ransomNote = "aa", magazine = "ab"))
print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
