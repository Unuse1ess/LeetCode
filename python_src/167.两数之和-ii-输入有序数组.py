#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import *

class Solution0:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        if size == 2:
            return [1, 2] 

        for l in range(size):
            num = target - numbers[l]
            a = l + 1
            b = size - 1
            while a <= b:
                mid = (a + b) >> 1
                if numbers[mid] < num:
                    a = mid + 1
                elif numbers[mid] > num:
                    b = mid - 1
                else:
                    return [l + 1, mid + 1]

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]
# @lc code=end

s = Solution()
print(s.twoSum(numbers = [2,3,4], target = 6))
print(s.twoSum(numbers = [-1,0], target = -1))
print(s.twoSum(numbers = [2,7,11,15], target = 9))
print(s.twoSum(numbers = list(range(-100, 101)), target = 198))
