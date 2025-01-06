#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from typing import *

# @lc code=start
class Solution:
    def getHist(self, words: List[str]):
        ret = dict()
        for w in words:
            ret[w] = ret.get(w, 0) + 1
        return ret

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = set()
        for i in range(len(words[0])):
            ret.update(i + j for j in self._findSubstring(s[i:], words))
        return list(ret)
            

    def _findSubstring(self, s: str, words: List[str]) -> List[int]:
        step = len(words[0])
        # size_w = len(words)
        size_s = len(s)

        hist = self.getHist(words)
        ret = []

        l, r = 0, 0
        while r + step <= size_s:
            subs = s[r: r + step]
            if subs in hist:
                hist[subs] -= 1
                while hist[subs] == -1:
                    hist[s[l: l + step]] += 1
                    l += step

                if all(hist[k] == 0 for k in hist):
                    ret.append(l)
                r += step
            else:
                if l != r:
                    hist = self.getHist(words)
                r += step
                l = r

        return ret

# @lc code=end

s = Solution()
print(s.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(s.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(s.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))
print(s.findSubstring(s = "aaaaaaaaaaaaaa", words = ["aa","aa"]))
print(s.findSubstring(s = "ababaab", words = ["ab","ba","ba"]))
print(s.findSubstring(s = "mississippi", words = ["si","is"]))
