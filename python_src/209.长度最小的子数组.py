#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import *

class Solution0:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        p_sum = [0 for _ in range(size + 1)]
        MAX = 1000000
        cnt = MAX
        for i in range(1, size + 1):
            p_sum[i] = p_sum[i - 1] + nums[i - 1]
        for i in range(size, 0, -1):
            n = p_sum[i] - target
            if n < 0:
                break
            l, r = 0, i - 1
            while l <= r:
                mid = (l + r) >> 1
                if p_sum[mid] <= n:
                    l = mid + 1
                    cnt = cnt if cnt < i - mid else i - mid
                elif p_sum[mid] > n:
                    r = mid - 1

        return cnt if cnt != MAX else 0

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        l, r = 0, -1
        s = 0
        MAX = 1000000
        cnt = MAX

        while True:
            if s < target:
                r += 1
                if r == size:
                    break
                s += nums[r]
            else:
                tmp = r - l + 1
                cnt = cnt if cnt < tmp else tmp
                s -= nums[l]
                l += 1

        return cnt if cnt != MAX else 0
        
# @lc code=end

s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(s.minSubArrayLen(target = 4, nums = [1,4,4]))
print(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
print(s.minSubArrayLen(target = 4, nums = [1,1,1,1,4]))
print(s.minSubArrayLen(target = 4, nums = [4,1,1,1,1]))
print(s.minSubArrayLen(11, nums = [1,2,3,4,5]))
print(s.minSubArrayLen(15, nums=[3, 8, 7, 2, 9]))


# import random
# s0 = Solution0()
# s1 = Solution()
# a, b = 0, 0
# l = None
# while a == b:
#     l = [random.randint(0, 10) for _ in range(5)]
#     a = s0.minSubArrayLen(15, l)
#     b = s1.minSubArrayLen(15, l)

# print(l)
# print(a, b)
