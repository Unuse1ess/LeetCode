#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List
from collections import defaultdict

class Solution0:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        pos = defaultdict(lambda: -k - 1)
        # pos = dict()
        for i, n in enumerate(nums):
            # if i - pos.get(n, -k - 1) <= k:
            if i - pos[n] <= k:
                return True
            pos[n] = i
        return False

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        size = len(nums)
        l, r = 0, 1
        note = set((nums[0],))

        while r < size:
            if nums[r] in note:
                return True
            note.add(nums[r])
            r += 1
            if r - l > k:
                note.remove(nums[l])
                l += 1
        return False
# @lc code=end

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 3))
print(s.containsNearbyDuplicate([1,2,2,3,4,5], 3))
