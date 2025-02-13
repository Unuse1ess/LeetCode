#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
from typing import *
from collections import *

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tmp = Counter(arr)
        return len(tmp) == len(set(tmp.values()))
# @lc code=end

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
