#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        note = {n}
        s = n
        while s != 1:
            tmp = 0
            for i in map(int, str(s)):
                tmp += i * i
            if tmp in note:
                return False
            s = tmp
            note.add(s)
        return True

# @lc code=end

s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))
