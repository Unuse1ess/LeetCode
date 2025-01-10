#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import *
from math import *

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(l1: int, r1: int, l2: int, r2: int, k: int) -> float:
            while True:
                step = k >> 1
                if step == 0: step = 1
                s1, s2 = r1 - l1, r2 - l2
                i1, i2 = l1 + step - 1, l2 + step - 1
                if s1 == 0:
                    v1 = None
                    d1 = 0
                else:
                    # v1 = nums1[r1 - 1] if i1 >= s1 else nums1[i1]
                    d1 = r1 - 1 if i1 >= s1 else i1
                    v1 = nums1[d1]
                    d1 = d1 - l1
                if s2 == 0:
                    v2 = None
                    d2 = 0
                else:
                    # v2 = nums2[r2 - 1] if i2 >= s2 else nums2[i2]
                    d2 = r2 - 1 if i2 >= s2 else i2
                    v2 = nums2[d2]
                    d2 = d2 - l2
                if v1 is not None and v2 is not None:
                    if v1 < v2:
                        if k == 1:
                            return v1
                        k -= d1 + 1
                        l1 += d1 + 1
                    else:
                        if k == 1:
                            return v2
                        k -= d2 + 1
                        l2 += d2 + 1
                elif v1 is not None and v2 is None:
                    return nums1[k]
                elif v1 is None and v2 is not None:
                    return nums2[k]
                

        m, n = len(nums1), len(nums2)
        tmp = (m + n) >> 1

        if (m + n) & 1 == 1:
            return find_kth(0, m, 0, n, tmp)
        else:
            return (find_kth(0, m, 0, n, tmp) +
                    find_kth(0, m, 0, n, tmp + 1)) / 2

        
# @lc code=end
# 1,2,2,3,4,5
# 1,3,5  2,4,6

s = Solution()
# print(s.findMedianSortedArrays([1,3], [2]))
# print(s.findMedianSortedArrays([1,2], [3,4]))
# print(s.findMedianSortedArrays([1,2,4], [3,5,6]))
print(s.findMedianSortedArrays(list(range(5)), list(range(5, 10))))
