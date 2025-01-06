#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        if numRows <= 1 or numRows >= size:
            return s

        get_step = lambda n: -2 + 2 * n
        ret = []

        for i in range(1, numRows + 1):
            step_l = get_step(numRows - i + 1)
            step_u = get_step(i)
            tmp = (step_l, step_u)
            
            j = i - 1
            idx = 0 if step_l != 0 else 1
            while j < size:
                # print(j, s[j], tmp[idx])
                ret.append(s[j])
                j += tmp[idx]
                if step_u == 0:
                    idx = 0
                elif step_l == 0:
                    idx = 1
                else:
                    idx ^= 1

        # print(ret)
        return ''.join(ret)

# @lc code=end

s = Solution()
assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert s.convert("A", 1) == "A"
