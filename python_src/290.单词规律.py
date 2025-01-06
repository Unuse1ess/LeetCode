#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        return len(pattern) == len(words) and \
            len(set(pattern)) == \
            len(set(words)) == \
            len(set(zip(pattern, words)))
# @lc code=end

s = Solution()
print(s.wordPattern("abba","dog cat cat dog"))
print(s.wordPattern("abba","dog cat cat fish"))
print(s.wordPattern("aaaa","dog cat cat dog"))
print(s.wordPattern("aba","cat cat cat dog"))
print(s.wordPattern("abaa","cat cat cat dog"))
