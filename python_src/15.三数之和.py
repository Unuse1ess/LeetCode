#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import *

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> Tuple[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return (l, r)
        return (-1, -2)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hist = {}
        ret = set()

        for n in nums:
            hist[n] = hist.get(n, 0) + 1
        keys = list(hist.keys())
        keys.sort()

        nums = []
        for n in keys:
            nums.extend([n] * (hist[n] if hist[n] < 3 else 3))

        size = len(nums)
        # print(nums)
        for i, n in enumerate(nums):
            l, r = i + 1, size
            while l < r:
                # print(l, r)
                a, b = self.twoSum(nums[l: r], -n)
                if a != -1:
                    a += l
                    b += l
                    # print(i, a, b)
                    # print((n, nums[a], nums[b]))
                    ret.add((n, nums[a], nums[b]))
                    l = a + 1
                    r = b
                else:
                    break

        return [list(i) for i in ret]
        
# @lc code=end

s = Solution()
# print(s.twoSum([-1, 0, 1, 2], 1))
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([-2,0,1,1,2]))
