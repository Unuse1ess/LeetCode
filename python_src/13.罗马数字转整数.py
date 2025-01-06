#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        last = 0
        for c in reversed(s):
            num += d[c] * (1 if d[c] >= last else -1)
            last = max(d[c], last)
        return num
# @lc code=end

s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))
