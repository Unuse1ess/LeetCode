#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret = 0
        flag = False
        for c in reversed(s):
            if c.isalpha():
                ret += 1
                flag = True
            if c == ' ' and flag:
                break

        return ret
# @lc code=end

s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))