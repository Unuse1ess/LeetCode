#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return size

        l, r = 0, 0
        cnt = 1
        table = set((s[0],))

        while True:
            r += 1
            if r >= size:
                break
            if s[r] not in table:
                table.add(s[r])
                tmp = r - l + 1
                cnt = cnt if cnt > tmp else tmp
            else:
                while s[r] in table:
                    table.remove(s[l])
                    l += 1
                table.add(s[r])

        return cnt
# @lc code=end

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("abcaacbb"))
print(s.lengthOfLongestSubstring("abccba"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
