#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import *
from math import *

class Solution0:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def find_kth(l1: int, l2: int, k: int) -> float:
            while True:
                step = k >> 1
                step = 1 if step == 0 else step

                k1 = l1 + step - 1
                k2 = l2 + step - 1

                if k1 < m:
                    v1 = nums1[k1]
                    step1 = step
                else:
                    if l1 < m:
                        v1 = nums1[m - 1]
                        step1 = m - l1
                    else:
                        v1 = None
                        step1 = 0
                if k2 < n:
                    v2 = nums2[k2]
                    step2 = step
                else:
                    if l2 < n:
                        v2 = nums2[n - 1]
                        step2 = n - l2
                    else:
                        v2 = None
                        step2 = 0

                if v1 is not None and v2 is not None:
                    if v1 < v2:
                        if k == 1:
                            return v1
                        k -= step1
                        l1 += step1
                    else:
                        if k == 1:
                            return v2
                        k -= step2
                        l2 += step2
                elif v1 is None:
                    return nums2[l2 + k - 1]
                else:
                    return nums1[l1 + k - 1]

        tmp = (m + n) >> 1

        if (m + n) & 1 == 1:
            return find_kth(0, 0, tmp + 1)
        else:
            return (find_kth(0, 0, tmp) +
                    find_kth(0, 0, tmp + 1)) / 2

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        INF = float("inf")
        median1, median2 = 0, 0
        l, r = 0, m
        while l <= r:
            i = (l + r) >> 1
            j = ((m + n + 1) >> 1) - i

            a_i = nums1[i] if i < m else INF
            a_im1 = nums1[i - 1] if i - 1 >= 0 else -INF
            b_j = nums2[j] if j < n else INF
            b_jm1 = nums2[j - 1] if j - 1 >= 0 else -INF

            if a_im1 <= b_j:
                median1, median2 = max(a_im1, b_jm1), min(a_i, b_j)
                l = i + 1
            else:
                r = i - 1
        return (median1 + median2) / 2 if ((m + n) & 1) == 0 else median1
# @lc code=end

s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))
print(s.findMedianSortedArrays([1,2], [3,4]))
print(s.findMedianSortedArrays([1,2,4], [3,5,6]))
print(s.findMedianSortedArrays(list(range(5)), list(range(5, 10))))
print(s.findMedianSortedArrays([0,0,0,0,0], [-1,0,0,0,0,0,1]))
print(s.findMedianSortedArrays([], [1]))
print(s.findMedianSortedArrays([], [1,2]))
print(s.findMedianSortedArrays([], [1,2,3]))
print(s.findMedianSortedArrays([], [1,2,3,4]))
