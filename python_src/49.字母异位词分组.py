#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
from collections import Counter, defaultdict

class Solution0:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        convert = lambda x: frozenset((k, x[k]) for k in x)
        ret = {convert(Counter(strs[0])): [strs[0]]}
        
        for i, s in enumerate(map(lambda t: convert(Counter(t)), strs[1:]), 1):
            lst = ret.get(s, [])
            lst.append(strs[i])
            ret[s] = lst
        # print(ret)

        return [ret[k] for k in ret]
        
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = ord('a')
        # size = len(strs)
        ret = defaultdict(list)
        for s in strs:
            hist = [0] * 26
            for c in map(lambda x: ord(x) - a, s):
                hist[c] += 1
            ret[tuple(hist)].append(s)

        return [ret[k] for k in ret]

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for i, s in enumerate(map(lambda x: ''.join(sorted(x)), strs)):
            ret[s].append(strs[i])
        return [ret[k] for k in ret]
# @lc code=end

s = Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(strs = ["a"]))
print(s.groupAnagrams(strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
print(s.groupAnagrams(strs = ["ddddddddddg","dgggggggggg"]))
