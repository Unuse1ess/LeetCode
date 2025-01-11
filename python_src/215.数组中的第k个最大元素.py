#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import *
from collections import *

class Solution0:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
        
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        buckets = [0] * 20001
        for n in nums:
            buckets[n + 10000] += 1
        i = 20000
        while k > 0:
            k -= buckets[i]
            i -= 1
        return i - 9999
        
# @lc code=end

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

## 3
print(s.findKthLargest([7,6,5,4,3,2,1], 5))

# print(s.findKthLargest([7,6,5,4,3,2,1], 1))
