#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import *
from functools import *
from collections import *

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        slen = len(s)
        jmp = defaultdict(list)
        dp: List[int] = [slen] * (slen + 1)
        dp[0] = 0

        min_len = min(len(w) for w in wordDict)

        for i in range(slen - min_len + 1):
            for word in wordDict:
                wlen = len(word)
                if i + wlen > slen or s[i] != word[0]:
                    continue
                if s[i: i + wlen] in wordDict:
                    jmp[i].append(wlen)

        if 0 not in jmp:
            return False
        
        for i in jmp:
            for j in jmp[i]:
                if dp[i] < dp[i + j]: dp[i + j] = dp[i]

        return dp[slen] == 0
# @lc code=end
        
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp: List[bool] = [None] * (n + 1)

        min_len = min(len(w) for w in wordDict)
        dp[:min_len] = (False,) * min_len
        dp[0] = True
        
        for i in range(min_len, n + 1):
            for j in range(i + 1 - min_len):
                dp[i] = dp[j] and s[j: i] in wordDict
                if dp[i]: break

        return dp[n]
        
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        min_len = min(len(w) for w in wordDict)

        @cache
        def dfs(i: int) -> bool:
            if i == n: return True
            for j in range(i + 1, n + 1):
                if s[i: j] in wordDict and dfs(j):
                    return True
            return False

        return dfs(0)

s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
