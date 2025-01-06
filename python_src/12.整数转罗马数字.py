#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        s = ''
        s_num = str(num)
        size = len(s_num)
        for i, digit in enumerate(s_num):
            n = int(digit)
            p = 10 ** (size - i - 1)
            base = n // 5
            tmp = offset = n % 5
            offset = mp[p] * offset if offset != 4 else mp[p] + mp[(n + 1) * p]
            base = mp[5 * base * p] * (0 if tmp == 4 else base)
            s += base + offset

        return s

# @lc code=end

s = Solution()
print(s.intToRoman(3749))
print(s.intToRoman(58))
print(s.intToRoman(1994))
