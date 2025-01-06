#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

class Solution0:
    def extract_par(self, s: str, start: int) -> slice | None:
        l, r = start, start
        lp, rp = 0, 0
        size = len(s)
        while r < size:
            if s[r] == '(':
                lp += 1
                l = r if lp == 0 else l
            elif s[r] == ')':
                rp += 1
            if lp != 0 and lp == rp:
                return slice(l + 1, r, 1)
            r += 1
    def calculate(self, s: str) -> int:
        size = len(s)
        l, r = 0, 0
        res = 0
        is_neg = 1
        while r < size:
            # if op2 is not None:
            #     op1 += op2
            #     op2 = None
            #     continue
            if s[r].isdigit():
                l = r
                while r < size and s[r].isdigit():
                    r += 1
                res += int(s[l: r]) * is_neg
                is_neg = 1
                continue
            if s[r] == '(':
                piece = self.extract_par(s, r)
                r = piece.stop + 1
                res += self.calculate(s[piece]) * is_neg
                is_neg = 1
                continue

            if s[r] == '-':
                is_neg = -1

            r += 1
        return res

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        size = len(s)
        sign_list = [1] # sign of respective parenthesis
        sign = 1
        res = 0

        l, r = 0, 0
        while r < size:
            if s[r].isdigit():
                l = r
                while r < size and s[r].isdigit():
                    r += 1
                res += int(s[l: r]) * sign_list[-1] * sign
                # a = int(s[l: r]) * sign_list[-1] * sign
                # res += a
                sign = 1
                continue

            if s[r] == '-':
                sign = -1
            elif s[r] == '(':
                sign_list.append(sign * sign_list[-1])
                sign = 1
            elif s[r] == ')':
                sign_list.pop()
                sign = 1
                # sign = sign_list[-1]

            r += 1
        return res
# @lc code=end

s = Solution()
print(s.calculate(s = "1 + 1"))
print(s.calculate(s = " 2-1 + 2 "))
print(s.calculate("1-(      -2)"))
print(s.calculate(s = "(1+(4+5+2)-3)+(6+8)"))
print(s.calculate(s = "(1-(4+5+2)-3)+(6+8)"))
print(s.calculate(s = "(1-(4-5+2)-3)-(6-8)-1-(-3)"))
