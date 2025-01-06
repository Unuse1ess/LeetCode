#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from typing import *
from itertools import *

# @lc code=start
class Solution:
    n2l: Dict[str, str] = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        slen = len(digits)
        if slen == 0: return []
        res = []
        def dfs(i: int, chs: List[str]):
            if i == slen:
                res.append(''.join(chs))
                return
            for c in Solution.n2l[digits[i]]:
                chs.append(c)
                dfs(i + 1, chs)
                chs.pop()
        dfs(0, [])
        return res
        
# @lc code=end

s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
