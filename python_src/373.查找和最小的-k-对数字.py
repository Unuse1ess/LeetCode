#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#
from typing import *
from heapq import *



# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res: List[List[int]] = []
        N1, N2 = len(nums1), len(nums2)
        
        # heap: List[Tuple[int, int, int]] = [(nums1[0] + nums2[0], 0, 0)]
        heap: List[Tuple[int, int, int]] = []
        for i in range(k if k < N1 else N1):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        i = 0
        while len(heap) > 0 and i < k:
            i += 1
            _, a, b = heappop(heap)
            # res.append([a, b])
            res.append([nums1[a], nums2[b]])
            if b + 1 < N2:
                heappush(heap, (nums1[a] + nums2[b + 1], a, b + 1))

        return res
        
# @lc code=end

s = Solution()
print(s.kSmallestPairs([1,7,11], [2,4,6], 3))
print(s.kSmallestPairs([1,1,2], [1,2,3], 2))
print(s.kSmallestPairs([1,7,11], [2,4,6], 9))
print(s.kSmallestPairs([1,1,2], [1,2,3], 9))
