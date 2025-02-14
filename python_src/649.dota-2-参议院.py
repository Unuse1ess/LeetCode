#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#
from typing import *
from collections import *

class Solution0:
    idx2w = ["Radiant", "Dire"]
    
    def predictPartyVictory(self, senate: str) -> str:
        r_snt = []
        d_snt = []
        for i, p in enumerate(senate):
            if p == "R": r_snt.append(i)
            else: d_snt.append(i)

        while len(r_snt) != 0 and len(d_snt) != 0:
            r_pos, d_pos = 0, 0 # Next banning senator
            while True:
                if r_snt[r_pos] < d_snt[d_pos]:
                    del d_snt[d_pos]
                    r_pos += 1
                else:
                    del r_snt[r_pos]
                    d_pos += 1

                if r_pos >= len(r_snt):
                    # Ban Radiant
                    tmp = len(d_snt) - d_pos
                    if tmp > len(r_snt): tmp = len(r_snt)
                    r_snt = r_snt[tmp:]
                    break
                elif d_pos >= len(d_snt):
                    # Ban Dire
                    tmp = len(r_snt) - r_pos
                    if tmp > len(d_snt): tmp = len(d_snt)
                    d_snt = d_snt[tmp:]
                    break

        return Solution.idx2w[len(d_snt) > 0]

class Solution:
    idx2w = ["Radiant", "Dire"]
    
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        r_snt = deque()
        d_snt = deque()
        for i, p in enumerate(senate):
            if p == "R": r_snt.append(i)
            else: d_snt.append(i)

        while len(r_snt) != 0 and len(d_snt) != 0:
            if r_snt[0] < d_snt[0]:
                r_snt.append(r_snt[0] + N)
            else:
                d_snt.append(d_snt[0] + N)
            r_snt.popleft()
            d_snt.popleft()

        return Solution.idx2w[len(d_snt) > 0]
# @lc code=end

s = Solution()
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))

## Dire
print(s.predictPartyVictory("DDRRR"))