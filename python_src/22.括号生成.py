#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import *

# @lc code=start
class Solution:
    template: List[str] = ["(", "", ")", ""]
    def generateParenthesis(self, n: int) -> List[str]:
        note: List[List[str]] = [[] for _ in range(n + 1)]

        note[0].append("")
        note[1].append("()")

        for i in range(2, n + 1):
            for j in range(i):
                k = i - j - 1
                for a in note[k]:
                    for b in note[j]:
                        Solution.template[1] = a
                        Solution.template[3] = b
                        note[i].append(''.join(Solution.template))
        return note[n]
                
# @lc code=end

s = Solution()
print([s.generateParenthesis(i) for i in range(1, 4)])
