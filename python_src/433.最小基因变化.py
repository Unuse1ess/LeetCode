#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from collections import *
from itertools import *
from typing import *

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene: return 0
        bank = set(bank)
        if endGene not in bank: return -1

        chekced = set()
        queue = deque()
        queue.append((startGene, 0))
        while len(queue) > 0:
            s, step = queue.popleft()
            for i in range(8):
                for j in "ACGT":
                    if s[i] == j: continue
                    tmp = s[:i] + j + s[i + 1:]
                    if tmp == endGene:
                        return step + 1
                    elif tmp in bank and tmp not in chekced:
                        queue.append((tmp, step + 1))
                        chekced.add(tmp)
        return -1
                    
# @lc code=end

s = Solution()
print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(s.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]))
print(s.minMutation("AACCGGTT", "AACCGGTA", []))
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
