#
# @lc app=leetcode.cn id=1679 lang=python3
#
# [1679] K 和数对的最大数目
#
from typing import *
from collections import *

class Solution0:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        cnt = 0
        note: DefaultDict[int, int] = defaultdict(int)
        for n in nums:
            if note[n] > 0:
                cnt += 1
                note[n] -= 1
            elif k >= n:
                note[k - n] += 1

        return cnt
        
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        note = Counter(nums)
        ret = 0
        half_k = k / 2
        for n in note:
            if n < half_k:
                ret += note[n] if note[n] < note[k - n] else note[k - n]
            elif n == half_k:
                ret += note[n] >> 1
        return ret
# @lc code=end

s = Solution()
print(s.maxOperations(nums = [1,2,3,4], k = 5))
print(s.maxOperations(nums = [3,1,3,4,3], k = 6))

## 4
print(s.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))